import streamlit as st
from prediction_helper import predict

# ------------ Page Config ------------
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    page_icon="🩺",
    layout="wide"
)

# ------------ CSS for Compact, Single-Page UI ------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
}

/* Compact Card */
.card {
    padding: 15px;
    border-radius: 14px;
    margin-bottom: 15px;
    background: var(--background-color);
    box-shadow: 0px 2px 10px rgba(0,0,0,0.06);
    border: 1px solid rgba(150,150,150,0.25);
}

/* Title inside card */
.card-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 12px;
    padding-bottom: 6px;
    border-bottom: 1px solid rgba(120,120,120,0.25);
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Predict Button */
.stButton>button {
    border-radius: 10px !important;
    padding: 8px 20px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Prediction Box */
.prediction-box {
    padding: 15px;
    border-radius: 10px;
    font-size: 18px;
    font-weight: 600;
    border-left: 6px solid #4CAF50;
}

</style>
""", unsafe_allow_html=True)

# ------------ Title ------------
st.markdown("<h2 style='text-align:center;'>🩺 Health Insurance Cost Predictor</h2>", unsafe_allow_html=True)
st.write("")

# ------------ Dropdown Options ------------
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure',
        'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
        'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# ============================================================
# SINGLE-PAGE LAYOUT — 2 COLUMN STRUCTURE (NO SCROLLING)
# ============================================================

left_col, right_col = st.columns(2, gap="medium")

# ---------- LEFT SIDE (Personal + Health Factors) ----------
with left_col:

    # Personal Info Block
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>🧍 Personal Information</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input('Age', min_value=18, max_value=100)
    with c2:
        number_of_dependants = st.number_input('Dependants', min_value=0, max_value=20)

    income_lakhs = st.number_input('Income in Lakhs', min_value=0, max_value=200)

    st.markdown("</div>", unsafe_allow_html=True)

    # Health Factors Block
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>💗 Health Factors</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        genetical_risk = st.number_input('Genetic Risk', min_value=0, max_value=5)
    with c2:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- RIGHT SIDE (Lifestyle + Insurance) ----------
with right_col:

    # Lifestyle & Region Block
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>🌍 Lifestyle & Region</div>", unsafe_allow_html=True)

    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])

    c1, c2 = st.columns(2)
    with c1:
        region = st.selectbox('Region', categorical_options['Region'])
    with c2:
        gender = st.selectbox('Gender', categorical_options['Gender'])

    st.markdown("</div>", unsafe_allow_html=True)

    # Insurance Details Block
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>💼 Insurance Details</div>", unsafe_allow_html=True)

    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])

    c1, c2 = st.columns(2)
    with c1:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
    with c2:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])

    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# ======================= PREDICTION ==========================
# ============================================================

input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

st.write("")
if st.button("Predict"):
    prediction = predict(input_dict)
    st.markdown(
        f"<div class='prediction-box'>🟢 Predicted Health Insurance Cost: <b>{prediction}</b></div>",
        unsafe_allow_html=True
    )
