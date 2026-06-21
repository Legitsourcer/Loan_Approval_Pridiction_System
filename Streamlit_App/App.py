import streamlit as st
import pandas as pd
import joblib
import base64
import os
# Load Model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "Model",
    "random_forest_model.pkl"
)

model = joblib.load(MODEL_PATH)



def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Glass effect container */
    .main-container {{
        background-color: rgba(255,255,255,0.88);
        padding: 25px;
        border-radius: 15px;
    }}

    h1 {{
        text-align: center;
        color: black;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# Change path if needed
set_background("..\Streamlit_App\image\loan.jpg")



st.markdown(
    """
    <h1 style='text-align: center; color: black;'>
        🏦 Loan Approval Prediction System
    </h1>
    """,
    unsafe_allow_html=True
)
st.write("Enter applicant details to predict loan approval status.")

   

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background-size:cover;
}

.main-card{
background: rgba(255,255,255,0.15);
backdrop-filter: blur(12px);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    married = st.selectbox(
        "Married",
        ["Yes","No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["0","1","2","3+"]
    )

    education = st.selectbox(
        "Education",
        ["Graduate","Not Graduate"]
    )

with col2:

    self_employed = st.selectbox(
        "Self Employed",
        ["Yes","No"]
    )

    property_area = st.selectbox(
        "Property Area",
        ["Urban","Semiurban","Rural"]
    )

    credit_history = st.selectbox(
        "Credit History",
        [1,0]
    )


st.subheader("💰 Financial Information")

col1, col2 = st.columns(2)

with col1:
    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0
    )

with col2:
    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0
    )

    loan_term = st.number_input(
        "Loan Term",
        value=360
    )
gender_map = {
    "Female": 0,
    "Male": 1
}

married_map = {
    "No": 0,
    "Yes": 1
}

education_map = {
    "Not Graduate": 0,
    "Graduate": 1
}

self_map = {
    "No": 0,
    "Yes": 1
}

property_map = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}

dependents_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3+": 3
}

if st.button("Predict Loan Status"):
     input_data= pd.DataFrame({
        'Gender': [gender_map[gender]],
        'Married': [married_map[married]],
        'Dependents': [dependents_map[dependents]],
        'Education': [education_map[education]],
        'Self_Employed': [self_map[self_employed]],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_map[property_area]]
    })

     prediction = model.predict(input_data)

     if prediction[0] == 1:
        st.success("✅ Loan Approved")
     else:
        st.error("❌ Loan Rejected")