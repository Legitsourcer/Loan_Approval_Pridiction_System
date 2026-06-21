# 🏦 Loan Approval Prediction System

## 📌 Project Overview

The Loan Approval Prediction System is a Machine Learning-based application that predicts whether a loan application should be approved or rejected based on applicant details. The project follows the complete Machine Learning Lifecycle, including data preprocessing, exploratory data analysis, feature engineering, model building, evaluation, and deployment using Streamlit.

---

## 🎯 Objective

To develop a predictive system that assists financial institutions in making faster and more accurate loan approval decisions by analyzing applicant information.

---

## 🗂 Dataset

**Source:** Kaggle Loan Prediction Dataset

### Features

* Gender
* Married
* Dependents
* Education
* Self Employed
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area

### Target Variable

* Loan Status

  * 1 = Approved
  * 0 = Rejected

---

## 🔄 Machine Learning Lifecycle

### Phase 1: Problem Understanding

* Defined business problem
* Identified project objectives
* Studied dataset structure

### Phase 2: Data Collection

* Downloaded dataset from Kaggle
* Analyzed dataset attributes

### Phase 3: Data Preprocessing

* Missing value treatment
* Duplicate removal
* Categorical encoding
* Data cleaning

### Phase 4: Exploratory Data Analysis (EDA)

Performed:

* Univariate Analysis
* Bivariate Analysis
* Correlation Analysis

Visualizations:

* Histograms
* Boxplots
* Scatter Plots
* Heatmaps

### Phase 5: Feature Engineering

Created:

* TotalIncome
* EMI

Performed feature selection and feature importance analysis.

### Phase 6: Model Building

Implemented and trained:

1. Logistic Regression
2. Random Forest Classifier
3. XGBoost Classifier

### Phase 7: Model Evaluation

Metrics Used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix
* ROC Curve

### Phase 8: Deployment

Developed an interactive web application using Streamlit that allows users to:

* Enter applicant details
* Predict loan approval status
* View results instantly

---

## 🏗 Project Structure

```text
Loan_Approval_Prediction_System/
│
├── Dataset/
│   ├── train.csv
│   ├── test.csv
│   └── processed_data.csv
│
├── Notebook/
│   ├── 01_Problem_Understanding.ipynb
│   ├── 02_Data_Collection.ipynb
│   ├── 03_Data_Preprocessing.ipynb
│   ├── 04_EDA.ipynb
│   ├── 05_Feature_Engineering.ipynb
│   ├── 06_Model_Building.ipynb
│   └── 07_Model_Evaluation.ipynb
│
├── Model/
│   ├── logistic_regression_model.pkl
│   ├── random_forest_model.pkl
│   └── xgboost_model.pkl
│
├── Streamlit_App/
│   ├── app.py
│   └── images/
│
├── Documentation/
│   ├── Project_Report.pdf
│   ├── PPT_Presentation.pptx
│   └── Screenshots/
│
└── README.md
```

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

---

## 📊 Model Performance

| Model               | Accuracy     |
| ------------------- | ------------ |
| Logistic Regression | 0.9844       |
| Random Forest       | 0.9844       |
| XGBoost             |  0.9906 <br> |

Best Performing Model: **XGBoost**

---

## 🚀 Running the Project

### Clone Repository

```bash
git clone https://github.com/Legitsourcer/Loan_Approval_Pridiction_System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
cd Streamlit_App
streamlit run app.py
```

---


---

## 🔮 Future Scope

* Integration with Banking APIs
* Cloud Deployment
* Deep Learning Models
* Mobile Application Development
* Real-time Credit Risk Assessment

---

## 📚 References

1. Kaggle Loan Prediction Dataset
2. Scikit-Learn Documentation
3. XGBoost Documentation
4. Streamlit Documentation

---

## 👨‍💻 Author

Akshay Srivastava

Machine Learning Project – Loan Approval Prediction System
