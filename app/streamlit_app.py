"""Warehouse throughput SLA dashboard — D07."""

import sys
from pathlib import Path

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from features import TARGET, prepare_features

st.set_page_config(page_title="sales-prediction-analytics-project", page_icon="🏭", layout="wide")

st.title("Sales Prediction Analytics Project")
st.caption("Which shifts meet throughput SLA? — VP Operations view")

DATA_PATH = Path("data/warehouse_throughput.csv")
MODEL_PATH = Path("models/model.joblib")

if not DATA_PATH.exists():
    st.warning("Dataset not found. Run `python src/train.py` first.")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["sla_label"] = df[TARGET].map({0: "Missed SLA", 1: "Meets SLA"})
shifts = sorted(df["shift"].unique().tolist())

st.sidebar.header("Filters")
selected_shifts = st.sidebar.multiselect("Shift", shifts, default=shifts)
min_units = st.sidebar.slider("Min units/hour", 0.0, float(df["units_per_hour"].max()), 0.0)
max_defect = st.sidebar.slider("Max defect rate", 0.0, float(df["defect_rate"].max()), float(df["defect_rate"].max()))

filtered = df[
    df["shift"].isin(selected_shifts)
    & (df["units_per_hour"] >= min_units)
    & (df["defect_rate"] <= max_defect)
]

sla_pct = filtered[TARGET].mean() * 100 if len(filtered) else 0
c1, c2, c3, c4 = st.columns(4)
c1.metric("Shifts analyzed", f"{len(filtered):,}")
c2.metric("SLA hit rate", f"{sla_pct:.1f}%")
c3.metric("Avg units/hr", f"{filtered['units_per_hour'].mean():.1f}" if len(filtered) else "—")
c4.metric("Avg defect rate", f"{filtered['defect_rate'].mean():.2f}" if len(filtered) else "—")

tab_ops, tab_quality, tab_predict = st.tabs(["Throughput", "Quality vs SLA", "SLA predictor"])

with tab_ops:
    fig_shift = px.box(
        filtered, x="shift", y="units_per_hour", color="sla_label",
        title="Units per hour by shift",
        color_discrete_map={"Meets SLA": "#27ae60", "Missed SLA": "#c0392b"},
    )
    st.plotly_chart(fig_shift, use_container_width=True)

    agg = filtered.groupby("shift", as_index=False).agg(
        units_avg=("units_per_hour", "mean"),
        sla_rate=(TARGET, "mean"),
        count=("shift_id", "count"),
    )
    fig_bar = px.bar(
        agg, x="shift", y="units_avg", color="sla_rate",
        title="Average throughput by shift (color = SLA rate)",
        color_continuous_scale="RdYlGn",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab_quality:
    fig_scatter = px.scatter(
        filtered, x="defect_rate", y="units_per_hour", color="sla_label",
        hover_data=["shift_id", "shift"], size="units_per_hour",
        title="Defect rate vs throughput (SLA outcome)",
        color_discrete_map={"Meets SLA": "#27ae60", "Missed SLA": "#c0392b"},
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    trend = filtered.sort_values("shift_id")
    fig_line = px.line(
        trend, x="shift_id", y="units_per_hour", color="shift",
        markers=True, title="Throughput trend across shift sequence",
    )
    st.plotly_chart(fig_line, use_container_width=True)

with tab_predict:
    if not MODEL_PATH.exists():
        st.info("Train a model first: `python src/train.py`")
    else:
        model = joblib.load(MODEL_PATH)
        X, _ = prepare_features(filtered)
        preds = model.predict(X)
        proba = model.predict_proba(X)[:, 1] if hasattr(model, "predict_proba") else preds.astype(float)

        result = filtered.copy()
        result["predicted_sla"] = preds
        result["p_meets_sla"] = proba

        at_risk = result[result["p_meets_sla"] < 0.5].sort_values("p_meets_sla")
        st.subheader("Shifts at SLA risk")
        if at_risk.empty:
            st.success("No shifts below 50% SLA confidence in current filter.")
        else:
            fig_risk = px.bar(
                at_risk.head(15), x="shift_id", y="p_meets_sla", color="shift",
                title="Lowest SLA confidence shifts",
                color_discrete_sequence=px.colors.qualitative.Set2,
            )
            st.plotly_chart(fig_risk, use_container_width=True)

        sel = st.selectbox("Inspect shift", result["shift_id"].astype(str).tolist())
        row = result[result["shift_id"].astype(str) == sel].iloc[0]
        m1, m2, m3 = st.columns(3)
        m1.metric("Shift", row["shift"])
        m2.metric("Units/hr", f"{row['units_per_hour']:.1f}")
        m3.metric("P(meets SLA)", f"{row['p_meets_sla']:.0%}")

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number", value=row["p_meets_sla"] * 100,
            title={"text": "SLA likelihood"},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#2980b9"}},
        ))
        st.plotly_chart(fig_gauge, use_container_width=True)
