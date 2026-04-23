# 🛒 Retail Sales Forecasting & Inventory Optimization System

An **end-to-end machine learning system** for **retail demand forecasting and inventory optimization**.  
The project predicts future sales using time-series models and recommends **optimal inventory decisions** such as **Reorder Point (ROP)**, **Safety Stock**, and **Order Quantity**.

It covers the **complete data science lifecycle**:
- Data ingestion & preprocessing  
- Feature engineering  
- Demand forecasting  
- Inventory optimization  
- Deployment via **Streamlit Dashboard** and **FastAPI**

---

## 🚀 Key Features

- 📈 **Time-Series Sales Forecasting**
- 🔄 **Intermittent Demand Handling** (Croston’s Method)
- 📦 **Inventory Optimization Logic**
  - Safety Stock (SS)
  - Reorder Point (ROP)
  - Economic Order Quantity (EOQ)
- 📊 **Interactive Streamlit Dashboard**
- 🌐 **REST API using FastAPI**
- 🧠 Modular, production-ready codebase

---

## 🧠 System Workflow

1. **Data Ingestion**
   - Load historical retail sales data
2. **Feature Engineering**
   - Lag features, rolling means, demand patterns
3. **Demand Forecasting**
   - Machine learning / statistical models
   - Croston method for intermittent demand
4. **Inventory Optimization**
   - Calculate Safety Stock
   - Compute Reorder Point
   - Suggest Order Quantity
5. **Deployment**
   - Streamlit dashboard for planners
   - FastAPI endpoint for integration

---

## 📁 Project Structure

```text

Retail_Sales_Forecasting_Inventory_Optimization_System/
│
├── api/
│   └── main.py
│       └── FastAPI application exposing inventory recommendations
│
├── dashboard/
│   └── app_streamlit.py
│       └── Interactive Streamlit dashboard for planners
│
├── data/
│   └── retail_timeseries.csv
│       └── Historical retail sales data
│
├── models/
│   └── retail_forecast_model.pkl
│       └── Trained forecasting model
│
├── notebooks/
│   └── EDA analysis.ipynb
│       └── Exploratory Data Analysis and insights
│
├── src/
│   ├── config.py
│   │   └── Global configuration variables
│   ├── data_ingestion.py
│   │   └── Data loading and validation
│   ├── feature_engineering.py
│   │   └── Feature creation for forecasting
│   ├── croston.py
│   │   └── Intermittent demand forecasting logic
│   ├── model_train.py
│   │   └── Model training and evaluation
│   ├── inventory.py
│   │   └── Inventory formulas (SS, ROP, EOQ)
│   └── pipeline.py
│       └── End-to-end pipeline (train → forecast → inventory)
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md

````

---

## ⚙️ Installation & Setup

```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
````

---

## 🏋️‍♂️ Run the Training Pipeline (Mandatory)

This step **trains the forecasting model** and saves it for later use.

```bash
python src/pipeline.py
```

📦 Output:

```
models/retail_forecast_model.pkl
```

---

## 📊 Run the Streamlit Dashboard

```bash
python -m streamlit run dashboard/app_streamlit.py
```

🔗 Open in browser:

```
http://localhost:8501
```

### Dashboard Inputs

* **On-hand inventory**
* **Lead time (days)**

### Dashboard Outputs

* Reorder Point (ROP)
* Recommended Order Quantity
* Inventory insights

---

## 🌐 Run the API (Optional)

```bash
python -m uvicorn api.main:app --reload
```

📘 API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Technologies Used

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Streamlit**
* **FastAPI**
* **Uvicorn**
* **Time-Series Forecasting**

---

## 🎯 Use Cases

* Retail inventory planning
* Demand forecasting for supply chains
* Academic & portfolio projects
* Decision support systems for operations

---

## 👤 Author

**Kusan Chakraborty**
B.Tech – Computer Science & Engineering (Data Science)

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to:

* Use
* Modify
* Distribute

This software, provided proper credit is given to the author.

© 2026 Kusan Chakraborty
