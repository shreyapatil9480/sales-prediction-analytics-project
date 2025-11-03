# Sales Prediction Analytics Project

This project showcases a **synthetic retail sales dataset** and a comprehensive analysis pipeline using Python. It is designed for professionals targeting roles in **business analysis**, **program management**, and **data analytics**. The repository includes:

- **Synthetic dataset:** Generated data simulating retail transactions, including product categories, quantities, pricing, discounts, customer demographics, revenue, and profit.
- **Jupyter notebook:** An analysis notebook demonstrating exploratory data analysis (EDA), data visualizations, feature engineering, and predictive modeling to classify transactions as high-profit or not.
- **Requirements file:** A list of Python dependencies to reproduce the environment.

## Repository Structure

```text
├── synthetic_sales_data.csv          # Synthetic retail dataset
├── sales_prediction_analysis.ipynb   # Analysis notebook with EDA and ML
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

## Getting Started

To explore this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shreyapatil9480/sales-prediction-analytics-project.git
   cd sales-prediction-analytics-project
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Open the notebook:**
   ```bash
   jupyter notebook sales_prediction_analysis.ipynb
   ```

The notebook will walk you through the data exploration and modeling process.

## Dataset Details

The synthetic dataset contains 1,000 retail transactions with the following columns:

| Column | Description |
| --- | --- |
| `order_id` | Unique identifier for each order |
| `order_date` | Date of the transaction |
| `region` | Geographic region (North, South, East, West) |
| `product_category` | Broad category of the product (Electronics, Furniture, Office Supplies, Clothing, Food & Beverage) |
| `product_subcategory` | Specific subcategory within the product category |
| `quantity` | Number of units purchased |
| `unit_price` | Price per unit (varies by category) |
| `discount` | Discount applied (0–30%) |
| `shipping_cost` | Shipping cost for the order |
| `customer_age_group` | Age group of the customer (18–25, 26–35, etc.) |
| `payment_method` | Payment method (Credit Card, Debit Card, Cash, PayPal, Gift Card) |
| `revenue` | Total revenue for the order (after discount) |
| `profit` | Profit earned from the order |
| `returned` | Indicates if the product was returned (1) or not (0) |
| `high_profit` | Target variable: 1 if profit is above the median, 0 otherwise |

## Predictive Modeling

The notebook demonstrates two classification models to predict the `high_profit` variable:

- **Logistic Regression:** A linear classifier used as a baseline.
- **Random Forest Classifier:** An ensemble method that captures non-linear relationships.

Model performance is evaluated using metrics such as accuracy, precision, recall, F1-score, and the confusion matrix.

## Extending the Project

Feel free to build upon this project by:

- Engineering additional features (e.g., time-based features, customer segmentation).
- Exploring regression models to predict continuous profit or revenue values.
- Implementing hyperparameter tuning and cross-validation.
- Deploying the trained model using a web framework (e.g., Flask or FastAPI).

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT), allowing you to use, modify, and distribute the code with attribution.

---
**Author:** Shreya Patil (shreyapatil9480)


*Note:* This branch includes the initial project files and demonstrates creating and analyzing a synthetic sales dataset for business analytics.
