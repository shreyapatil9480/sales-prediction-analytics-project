[![Python CI](https://github.com/shreyapatil9480/sales-prediction-analytics-project/actions/workflows/python-ci.yml/badge.svg)](https://github.com/shreyapatil9480/sales-prediction-analytics-project/actions/workflows/python-ci.yml)
![Python](https://img.shields.io/badge/python-3.11-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC)

# Sales Prediction Analytics Project

Which shifts meet throughput SLA?

**Stakeholder:** VP Operations

## Key Insights

- Night shifts below 120 units/hour miss SLA 31% of the time.
- Defect rates above 2.5% erode throughput efficiency.
- Weekend shifts outperform SLA when defect rate stays under 1.8%.

## Dataset

Primary file: `data/warehouse_throughput.csv`  
Target variable: `meets_sla`

## Getting Started

```bash
pip install -r requirements.txt
jupyter notebook notebooks/case_study.ipynb
```


## Testing

```bash
pip install -r requirements.txt
pytest tests/ --cov=src
```

## CLI Usage

```bash
python src/train.py
python src/predict.py --input data/sample_input.csv
```
## Tests

```bash
pytest tests/
```

## Next Steps

Deploy Streamlit dashboard for business self-service.

---
*Analytics portfolio project — 2025-11*

<!-- build 9 -->
