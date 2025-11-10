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

## CLI Usage

```bash
python src/train.py
python src/predict.py --input data/sample_input.csv
```
## Tests

```bash
pytest tests/
```
