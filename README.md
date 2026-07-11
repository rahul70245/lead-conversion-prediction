#  Lead Conversion Prediction System

An end-to-end Machine Learning project that predicts whether a lead will convert into a customer at different stages of the sales pipeline.

The project covers the complete ML lifecycle, including data extraction from SQL, feature engineering, model experimentation, threshold optimization, API development using FastAPI, and deployment-ready model serving.

---

#  Problem Statement

Sales teams spend a significant amount of time following up with leads that may never convert.

This project helps prioritize leads by predicting conversion probability at different stages of the sales process.

Three different prediction models were built:

- **Source Model** – Predicts conversion immediately after lead creation.
- **Assigned Model** – Predicts conversion once a lead has been assigned to an owner.
- **Dynamic Model** – Predicts conversion using complete interaction history including calls and engagement metrics.

---


#  Business Impact

The Lead Conversion Prediction System helps sales teams focus on high-value leads instead of treating every lead equally.

By predicting the probability of conversion at multiple stages of the sales pipeline, the system enables data-driven decision making and improves sales efficiency.

### Business Benefits

- Prioritizes leads that are more likely to convert.
- Reduces time spent on low-quality leads.
- Improves follow-up planning for sales representatives.
- Enables better allocation of sales resources.
- Supports managers in monitoring lead quality across different lead sources.
- Provides real-time conversion predictions through REST APIs.
- Can be integrated into CRM systems to automate lead scoring and prioritization.

### Expected Business Outcomes

- Increased sales team productivity.
- Faster response to high-potential leads.
- Better lead qualification process.
- Improved conversion rates through intelligent prioritization.
- Data-driven decision making instead of manual lead selection.

---


#  Project Architecture

```
Database
      │
      ▼
SQL Dataset Creation
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Threshold Optimization
      │
      ▼
FastAPI
      │
      ▼
Deployment
```

---

#  Project Structure

```
lead-conversion-prediction/

│
├── api/
│   ├── main.py
│   ├── config.py
│   ├── predictor.py
│   ├── schemas.py
│   │
│   ├── routes/
│   │      predict.py
│   │
│   ├── services/
│   │      model_service.py
│   │
│   └── __init__.py
│
├── models/
│      thresholds.json
│
├── notebooks/
│      01_database_connection.ipynb
│      02_dataset_creation.ipynb
│      03_eda.ipynb
│      04_feature_engineering.ipynb
│      05_model_training.ipynb
│      06_model_selection.ipynb
│      07_model_saving.ipynb
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

#  Dataset

The dataset was created from a production-like SQL database containing multiple business tables.

### Tables Used

- Leads
- Calls
- Contacts
- PII
- Orders

The final dataset was generated completely using SQL and Python.

---

#  Features

### Source Model

- Lead Source

---

### Assigned Model

- Lead Source
- Owner
- Assigned Month
- Assigned Year

---

### Dynamic Model

Includes complete lead engagement history.

- Owner
- Lead Source
- Profile
- Total Duration
- Call Count
- Connected Calls
- Missed Calls
- Distinct Call Days
- Average Duration
- Connection Rate
- Miss Rate
- Follow-up Done
- Average Calls Per Day
- Call Span
- Call Frequency
- Inbound / Outbound Ratio
- Time Taken For First Touch
- Assigned Month
- Assigned Year

---

#  Models Used

The following algorithms were evaluated.

- Logistic Regression
- Random Forest
- XGBoost

---

#  Experiments Performed

The project compares multiple approaches.

### Baseline Models

Standard model training without any modifications.

---

### Balanced Models

Training using

```
class_weight='balanced'
```

to handle class imbalance.

---

### Power Transformation

Applied Power Transformer on numerical features.

---

### Hyperparameter Tuning

Performed GridSearchCV using

```
ROC-AUC
```

as the optimization metric.

---

### Threshold Optimization

Instead of using the default threshold of **0.50**, different thresholds were evaluated to achieve the best business trade-off between Precision and Recall.

Thresholds tested

```
0.30

0.35

0.40

0.45

0.50

0.55

0.60

0.65

0.70
```

---

#  Final Models

After evaluating multiple experiments, Logistic Regression was selected for all three prediction stages.

Selection criteria

- ROC-AUC
- F1 Score
- Business Recall
- Model Simplicity
- Faster Inference

Final Thresholds

| Model | Threshold |
|--------|-----------|
| Source | 0.40 |
| Assigned | 0.40 |
| Dynamic | 0.45 |

---

# 🚀 API

The project exposes prediction endpoints using FastAPI.

### Endpoints

```
POST /predict/source

POST /predict/assigned

POST /predict/dynamic
```

---

Example Request

```json
{
    "lead_source":"IndiaMart"
}
```

Example Response

```json
{
    "prediction":1,
    "probability":0.83,
    "threshold":0.40
}
```

---

#  Tech Stack

### Languages

- Python
- SQL

### Machine Learning

- Scikit-Learn
- XGBoost
- Imbalanced-Learn

### Data Processing

- Pandas
- NumPy

### API

- FastAPI
- Uvicorn
- Pydantic

### Model Storage

- Joblib

---

#  Key Learnings

- End-to-end ML pipeline development
- SQL-based dataset creation
- Feature engineering
- Handling imbalanced datasets
- Hyperparameter tuning
- Threshold optimization
- Pipeline-based model deployment
- REST API development using FastAPI
- Production-ready project structure

---

# ▶ Running the Project

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn api.main:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# 👨‍💻 Author

**Rahul Moolchandani**

Data Analyst | Machine Learning Enthusiast

LinkedIn: linkedin.com/in/rahul-moolchandani-998a85282

GitHub: github.com/rahul70245

EDA HTML DEPLOYED LINK: https://rahul70245.github.io/lead-conversion-prediction/eda.html

---

⭐ If you found this project useful, consider giving it a star.