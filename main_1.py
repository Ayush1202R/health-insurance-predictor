import streamlit as st
from prediction_helper import predict

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    layout="wide"
)

# ---------------- CSS: Remove empty containers + clean style ----------------
st.markdown("""
<style>

div[data-testid="stVerticalBlock"] > div:empty {
    display: none !important;
}
div[data-testid="column"] > div:empty {
    display: none !important;
}

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
}

/* Clean heading with perfect line under it */
.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 4px;
    padding-bottom: 6px;
    border-bottom: 1px solid rgba(255,255,255,0.18);
}

</style>
""", unsafe_allow_html=True)

# ---------------- Main Title ----------------
st.markdown("<h2 style='text-align:center;'>Health Insurance Cost Predictor</h2>", unsafe_allow_html=True)

# ---------------- Dropdown Options ----------------
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer'],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure',
        'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
        'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# ================= Layout (Two Columns) =================
left_col, right_col = st.columns(2, gap="large")

# ---------------- LEFT SIDE ----------------
with left_col:

    # PERSONAL INFORMATION
    st.markdown("<div class='section-title'>Personal Information</div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    age = c1.number_input('Age', min_value=18, max_value=100)
    dependants = c2.number_input('Dependants', min_value=0, max_value=20)

    income = st.number_input('Income in Lakhs', min_value=0, max_value=100)

    # HEALTH FACTORS
    st.markdown("<div class='section-title'>Health Factors</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    genetical_risk = c1.number_input('Genetic Risk', min_value=0, max_value=5)
    bmi_category = c2.selectbox('BMI Category', categorical_options['BMI Category'])

    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])


# ---------------- RIGHT SIDE ----------------
with right_col:

    # LIFESTYLE & REGION
    st.markdown("<div class='section-title'>Lifestyle & Region</div>", unsafe_allow_html=True)

    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])

    c1, c2 = st.columns(2)
    region = c1.selectbox('Region', categorical_options['Region'])
    gender = c2.selectbox('Gender', categorical_options['Gender'])

    # INSURANCE DETAILS
    st.markdown("<div class='section-title'>Insurance Details</div>", unsafe_allow_html=True)

    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])

    c1, c2 = st.columns(2)
    employment_status = c1.selectbox('Employment Status', categorical_options['Employment Status'])
    marital_status = c2.selectbox('Marital Status', categorical_options['Marital Status'])


# ================= Prediction =================
input_dict = {
    'Age': age,
    'Number of Dependants': dependants,
    'Income in Lakhs': income,
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

if st.button("Predict"):
    prediction = predict(input_dict)
    st.success(f"Predicted Health Insurance Cost: {prediction}")
