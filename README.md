# 📉 Customer Churn Analysis

A Python-based customer churn analysis project that examines customer behaviour to understand churn patterns and identify differences between customers who stay and customers who leave.

The project uses **Pandas** for data analysis and **Matplotlib** for visualization.

---

## 📌 Project Overview

Customer churn is an important business problem because understanding why customers leave can help organizations improve retention.

This project analyzes customer-level data to calculate:

* Total customers
* Customers who churned
* Overall churn rate
* Average monthly usage
* Average support calls
* Churn distribution

---

## 🎯 Objectives

The project aims to:

* Understand the proportion of customers who leave.
* Compare usage behaviour between retained and churned customers.
* Compare support-call behaviour between customer groups.
* Visualize churn distribution.
* Produce a processed dataset for further analysis.

---

## 🔄 Analysis Workflow

```text
Customer Dataset
       ↓
Load CSV
       ↓
Inspect Data
       ↓
Check Missing Values
       ↓
Calculate Customer Metrics
       ↓
Analyze Churn
       ↓
Compare Behaviour
       ↓
Visualize Churn
       ↓
Export Results
```

---

## 📊 Key Metrics

### Total Customers

Number of customers present in the dataset.

### Churned Customers

Number of customers where:

```text
Churn = 1
```

### Churn Rate

```text
Churn Rate =
(Churned Customers / Total Customers) × 100
```

### Behaviour Analysis

The project compares:

* Average monthly usage
* Average support calls

between customers who stayed and customers who churned.

---

## 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib
* CSV

---

## 📂 Project Structure

```text
Customer-Churn-Analysis/
│
├── churn_analysis.py
├── customer_data.csv
├── churn_result.csv
└── README.md
```

---

## 🚀 Getting Started

### Clone

```bash
git clone https://github.com/sathwik-131/Customer-Churn-Analysis.git
cd Customer-Churn-Analysis
```

### Install dependencies

```bash
pip install pandas matplotlib
```

### Run

```bash
python churn_analysis.py
```

The program loads the customer dataset, calculates churn metrics, generates a churn visualization, and exports the processed data.

---

## 🧠 Skills Demonstrated

* Python
* Pandas
* DataFrame operations
* GroupBy analysis
* Churn-rate calculation
* Customer behaviour analysis
* Data visualization
* CSV processing
* Basic data-quality inspection

---

## 🔮 Future Improvements

The project can be extended into a complete churn prediction system by adding:

* Feature engineering
* Logistic Regression
* Decision Trees
* Random Forest
* Model evaluation
* Confusion matrix
* Precision / Recall / F1-score
* Feature importance
* Customer churn probability
* Streamlit dashboard
* Churn prediction API

---

## ⚠️ Scope

This repository currently performs **descriptive customer churn analysis**. It does not train a machine-learning model or predict future churn.

---

## 👨‍💻 Author

**Sathwik B**

B.Tech — Computer Science & Machine Learning

GitHub: [@sathwik-131](https://github.com/sathwik-131)

---

## 📌 Project Status

**Completed — Foundational Customer Analytics Project**
