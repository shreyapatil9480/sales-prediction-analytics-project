"""Feature engineering for D07."""

import pandas as pd


FEATURE_COLUMNS = ['shift', 'units_per_hour', 'defect_rate']
TARGET = "meets_sla"


def prepare_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Select model features and target."""
    X = df[FEATURE_COLUMNS].copy()
    for col in X.select_dtypes(include="object").columns:
        X[col] = X[col].astype("category").cat.codes
    y = df[TARGET]
    return X, y
