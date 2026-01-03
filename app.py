import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

st.write("Enter customer details to predict churn risk.")

# ---- Input fields ----
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)

PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

numAdminTickets = st.number_input("Admin Tickets", 0, 20, 0)
numTechTickets = st.number_input("Tech Tickets", 0, 20, 0)

# ---- Predict ----
if st.button("Predict Churn"):
    # Binary mapping (same as training)
    binary_map = {
        "Yes": 1, "No": 0,
        "Male": 1, "Female": 0
    }
    
    input_data = pd.DataFrame([{
        "gender": binary_map[gender],  # Convert to int
        "SeniorCitizen": SeniorCitizen,
        "Partner": binary_map[Partner],  # Convert to int
        "Dependents": binary_map[Dependents],  # Convert to int
        "tenure": tenure,
        "PhoneService": binary_map[PhoneService],  # Convert to int
        "MultipleLines": MultipleLines,  # Keep as categorical
        "InternetService": InternetService,  # Keep as categorical
        "OnlineSecurity": OnlineSecurity,  # Keep as categorical
        "OnlineBackup": OnlineBackup,  # Keep as categorical
        "DeviceProtection": DeviceProtection,  # Keep as categorical
        "TechSupport": TechSupport,  # Keep as categorical
        "StreamingTV": StreamingTV,  # Keep as categorical
        "StreamingMovies": StreamingMovies,  # Keep as categorical
        "Contract": Contract,  # Keep as categorical
        "PaperlessBilling": binary_map[PaperlessBilling],  # Convert to int
        "PaymentMethod": PaymentMethod,  # Keep as categorical
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "numAdminTickets": numAdminTickets,
        "numTechTickets": numTechTickets
    }])

    churn_prob = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")
    st.write(f"Churn Probability: **{churn_prob:.2%}**")

    if churn_prob >= 0.47:  # Use same threshold as training (0.47)
        st.error("⚠️ High risk of churn")
    else:
        st.success("✅ Low risk of churn")