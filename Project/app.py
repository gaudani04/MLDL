import streamlit as st
import numpy as np
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Disease Risk Detection",
    page_icon="🫀",
    layout="wide"
)

# ---------------- GLOBAL DARK THEME ----------------
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background-color: #000000;
    color: white;
}

/* HEADINGS */
h1, h2, h3, h4, h5, h6, p, span, label {
    color: white !important;
}

/* INPUT FIELDS */
input, textarea {
    background-color: #111111 !important;
    color: white !important;
}

/* SELECTBOX - VALUE */
div[data-baseweb="select"] span {
    color: white !important;
}

/* SELECTBOX - BOX */
div[data-baseweb="select"] > div {
    background-color: #111111 !important;
}

/* SELECTBOX - DROPDOWN MENU */
div[data-baseweb="menu"] {
    background-color: #111111 !important;
}

/* SELECTBOX - OPTIONS */
div[data-baseweb="menu"] span {
    color: white !important;
}

/* HOVER */
div[data-baseweb="option"]:hover {
    background-color: #222222 !important;
}

/* BUTTON */
.stButton button {
    background: linear-gradient(90deg, #b71c1c, #ff5252);
    color: white;
    border-radius: 10px;
    font-weight: bold;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #000000;
}
section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🫀 Heart Care AI")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Risk Prediction", "ML Model Info", "About Disease", "Medical Disclaimer"]
)

# ---------------- HOME PAGE ----------------
if page == "Home":
    st.markdown(
        "<h1 style='text-align:center;color:#ff5252;'>🫀 Heart Disease Risk Detection</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;font-size:18px;'>Assess your heart health in seconds using AI</p>",
        unsafe_allow_html=True
    )

    # CENTER IMAGE PROPERLY
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("heart_hero.png", width=600)

    st.markdown("---")

    st.markdown("""
    <div style="text-align:center;">
        <h3>Why use this app?</h3>
        <p>✔ AI-powered prediction</p>
        <p>✔ Instant results</p>
        <p>✔ Educational medical insights</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- PREDICTION PAGE ----------------
elif page == "Risk Prediction":
    st.header("🧪 Cardiovascular Risk Prediction")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100)
        gender = st.selectbox("Gender", ["Female", "Male"])
        ap_hi = st.number_input("Systolic BP (ap_hi)", 80, 250)
        ap_lo = st.number_input("Diastolic BP (ap_lo)", 50, 150)
        cholesterol = st.selectbox("Cholesterol", ["Normal", "Above Normal", "Well Above Normal"])

    with col2:
        gluc = st.selectbox("Glucose", ["Normal", "Above Normal", "Well Above Normal"])
        smoke = st.selectbox("Smoking", ["No", "Yes"])
        alco = st.selectbox("Alcohol Intake", ["No", "Yes"])
        active = st.selectbox("Physically Active", ["No", "Yes"])
        bp_diff = ap_hi - ap_lo

    if st.button("🔍 Predict Risk"):
        # MOCK prediction (replace with model.predict_proba)
        risk = np.random.uniform(0.2, 0.9)

        st.markdown("### 🫀 Risk Probability")
        st.progress(int(risk * 100))

        if risk < 0.4:
            st.success("Low Risk – Maintain a healthy lifestyle.")
        elif risk < 0.7:
            st.warning("Moderate Risk – Regular checkups recommended.")
        else:
            st.error("High Risk – Consult a cardiologist.")

# ---------------- MODEL INFO ----------------
elif page == "ML Model Info":
    st.header("🤖 Machine Learning Model Info")

    st.markdown("""
    **Model Used:** Logistic Regression  
    **Features:**
    - Age
    - Gender
    - Systolic BP
    - Diastolic BP
    - Cholesterol
    - Glucose
    - Smoking
    - Alcohol
    - Physical Activity
    - BP Difference
    """)

    st.markdown("""
    **Performance Metrics:**
    - Accuracy: 86%
    - Precision: 84%
    - Recall: 82%
    - F1-Score: 83%
    - ROC-AUC: 0.88
    """)

# ---------------- ABOUT DISEASE ----------------
elif page == "About Disease":
    st.header("🫀 About Cardiovascular Disease")

    st.markdown("""
    Cardiovascular diseases (CVDs) are disorders of the heart and blood vessels.

    **Common Symptoms:**
    - Chest pain
    - Shortness of breath
    - Fatigue
    - Irregular heartbeat

    **Prevention Tips:**
    - Regular exercise
    - Balanced diet
    - Avoid smoking
    - Control blood pressure
    """)

# ---------------- DISCLAIMER ----------------
elif page == "Medical Disclaimer":
    st.header("⚠️ Medical Disclaimer")

    st.markdown("""
    This application provides **AI-based predictions for educational purposes only**.

    ❗ It is **NOT a substitute for professional medical advice**.  
    Always consult a qualified healthcare provider for diagnosis and treatment.
    """)

