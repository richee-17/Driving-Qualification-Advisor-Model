import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from pdf_generator import generate_pdf

st.set_page_config(page_title="Try It Yourself", layout="wide")

st.title("\U0001F9EA Try It Yourself - Driving Qualification Prediction")
st.markdown("Input your driving details and check if you are qualified based on the AI model.")
st.markdown("---")

# Load model
with open("driving_model.pkl", "rb") as f:
    model = pickle.load(f)

# Input Layout
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown("### \U0001F464 Demographics")
    gender = st.selectbox("Gender", ["Female", "Male"])
    age_group = st.selectbox("Age Group", ["Teenager", "Young Adult", "Middle Age"])
    race = st.selectbox("Race", ["Other", "White", "Black"])
    training = st.radio("Training Level", ["Basic", "Advanced"], horizontal=True)
    reactions = st.radio("Reactions", ["Slow", "Fast"], horizontal=True)

with col2:
    st.markdown("### \u2699\ufe0f Driving Skills")
    signals = st.slider("Signals", 0, 100, 50)
    yield_score = st.slider("Yield", 0, 100, 50)
    speed_control = st.slider("Speed Control", 0, 100, 50)
    night_drive = st.slider("Night Drive", 0, 100, 50)
    road_signs = st.slider("Road Signs", 0, 100, 50)

with col3:
    st.markdown("### \U0001F9E0 Other Factors")
    steer_control = st.slider("Steer Control", 0, 100, 50)
    mirror_usage = st.slider("Mirror Usage", 0, 100, 50)
    confidence = st.slider("Confidence", 0, 100, 50)
    parking = st.slider("Parking", 0, 100, 50)
    theory_test = st.slider("Theory Test", 0, 100, 50)

# Encode categorical
gender = 1 if gender == "Male" else 0
age_group = {"Teenager": 0, "Young Adult": 1, "Middle Age": 2}[age_group]
race = {"Other": 0, "White": 1, "Black": 2}[race]
training = 1 if training == "Advanced" else 0
reactions = 1 if reactions == "Fast" else 0

# Prepare input
data = np.array([[gender, age_group, race, training,
                  signals, yield_score, speed_control, night_drive, road_signs,
                  steer_control, mirror_usage, confidence, parking, theory_test,
                  reactions]])

# Predict
if st.button("\U0001F50D Predict My Qualification"):
    prediction = model.predict(data)[0]

    result_text = "You are Qualified!" if prediction == 1 else "You are Not Qualified."
    pdf_result = result_text

    st.markdown("### \U0001F3AF Prediction Result")
    if prediction == 1:
        st.success("\u2705 " + result_text)
    else:
        st.error("\u274C " + result_text)

    st.markdown("### \U0001F4CA Your Input Feature Breakdown")
    labels = [
        "Gender", "Age Group", "Race", "Training", "Signals", "Yield",
        "Speed Control", "Night Drive", "Road Signs", "Steer Control",
        "Mirror Usage", "Confidence", "Parking", "Theory Test", "Reactions"
    ]

    fig, ax = plt.subplots(figsize=(9, 6))
    sns.set_style("whitegrid")
    sns.barplot(x=data[0], y=labels, palette="pastel", ax=ax)
    ax.set_xlim(0, 100)
    ax.set_title("Your Input Feature Scores")
    st.pyplot(fig)

    st.info("\U0001F4C4 You can now download your full prediction details as a PDF report.")

    pdf_bytes = generate_pdf(data, labels, pdf_result)
    st.download_button(
        label="\U0001F4E5 Download PDF Report",
        data=pdf_bytes,
        file_name="driving_prediction_report.pdf",
        mime="application/pdf"
    )

    st.caption("\U0001F5A8 Tip: Open the PDF after downloading and press Ctrl+P to print.")
