import streamlit as st

st.set_page_config(page_title="Driving Qualification Advisor", layout="centered")

# Main Heading
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🚗 Driving Qualification Advisor</h1>", unsafe_allow_html=True)
st.image("https://cdn-icons-png.flaticon.com/512/743/743007.png", width=300)


# Intro Section
st.markdown("""
### 👋 Welcome!
This interactive AI-powered platform helps you assess your **driving qualification level** based on various performance and training indicators.

Built using **Machine Learning**, this tool simulates real-world driving evaluations to help drivers:
- Understand their driving strengths
- Identify areas for improvement
- Get AI feedback instantly and visually

---

### 🧭 What You Can Do Here:
#### 💡 Try the AI Prediction
> Submit your scores on driving aspects like confidence, road signs, speed control, etc., and instantly know if you are **qualified or not**.

#### 📊 Explore the Dataset
> Dive into the actual dataset and see how others performed. We’ve visualized:
- Gender & Age Group trends
- Training level impact
- Qualification distributions

#### 🔍 Understand the Model
> Learn how our **Random Forest Classifier** works behind the scenes:
- Which features are most important?
- What’s the model accuracy?
- How were the predictions trained?

#### 📬 Leave Feedback
> Want to report an issue or suggest an improvement? Use our **contact form** to reach out.

---

### ✅ Get Started Now!
👉 Use the sidebar to navigate to **“🧪 Try It Yourself”** and begin your qualification check.
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("🔧 Built with Python, Streamlit, and Machine Learning | By Richee Chabhadiyia")

