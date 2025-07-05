import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

st.title("🔍 About the Model")

st.markdown("""
### ✅ Model Overview: Random Forest Classifier
Our **Random Forest Classifier** is designed to predict whether a driver is **qualified (1)** or **not qualified (0)** based on multiple driving-related features.

- **Training Data:** Collected from driving tests assessing various skills and demographic information.
- **Features:** 15 different attributes including demographic data and detailed driving metrics.
- **Performance:** Achieved an impressive accuracy of **91%** on unseen test data, demonstrating strong predictive capabilities.

---

### 🔢 Features Used for Prediction:
| Feature Name     | Description                          |
|------------------|------------------------------------|
| Gender           | Driver's gender                    |
| Age Group        | Age category (e.g., 18-25, 26-35) |
| Race             | Driver's race/ethnicity            |
| Training         | Level of driving training          |
| Signals          | Use of turn signals                |
| Yield            | Ability to yield properly          |
| Speed Control    | Control over vehicle speed         |
| Night Drive      | Performance in night driving       |
| Road Signs       | Knowledge & adherence to signs     |
| Steer Control    | Smoothness in steering             |
| Mirror Usage     | Frequency and effectiveness       |
| Confidence       | Confidence level behind the wheel  |
| Parking          | Skill in parking maneuvers         |
| Theory Test      | Score on theoretical driving test |
| Reactions        | Reaction time and decision making  |

---

### 📊 Feature Importance Analysis
The plot below shows the relative importance of each feature as determined by the Random Forest model. Features with higher importance have a stronger influence on the model's decision-making process.

""")

# Load model
with open("driving_model.pkl", "rb") as f:
    model = pickle.load(f)

features = [
    "Gender", "Age Group", "Race", "Training", "Signals", "Yield",
    "Speed Control", "Night Drive", "Road Signs", "Steer Control",
    "Mirror Usage", "Confidence", "Parking", "Theory Test", "Reactions"
]

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=True)

fig, ax = plt.subplots(figsize=(10, 7))
sns.barplot(x="Importance", y="Feature", data=importance_df, palette="Blues_d", ax=ax)
plt.title("Feature Importances in Random Forest Model", fontsize=16)
plt.xlabel("Importance Score", fontsize=14)
plt.ylabel("Features", fontsize=14)
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# For better explanation, add confusion matrix and classification report
st.markdown("""
### 📈 Model Evaluation Metrics

Below are additional metrics to give you a more comprehensive understanding of the model's performance beyond accuracy.

- **Confusion Matrix:** Shows how many predictions were true positives, true negatives, false positives, and false negatives.
- **Classification Report:** Includes precision, recall, and F1-score for each class.

""")

# Assume you have test data loaded for evaluation (replace with actual test data)
# Here, for demonstration, generating dummy y_true and y_pred
# In practice, load your test labels and predicted labels
y_true = np.random.choice([0, 1], size=100, p=[0.4, 0.6])
y_pred = model.predict(np.random.rand(100, 15))  # Replace with real test features

# Confusion Matrix plot
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Example data (replace with actual predictions)
y_true = [0]*26 + [1]*44     # 26 not qualified, 44 qualified
y_pred = [0]*14 + [1]*12 + [0]*2 + [1]*42  # matching your image

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Create heatmap
fig, ax = plt.subplots(figsize=(4, 3))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', 
            annot_kws={"size": 16}, linewidths=1, linecolor='white')

# Set labels
ax.set_xlabel("Predicted", fontsize=12)
ax.set_ylabel("Actual", fontsize=12)
ax.xaxis.set_ticklabels(['0', '1'], fontsize=11)
ax.yaxis.set_ticklabels(['0', '1'], fontsize=11)
ax.set_title("Confusion Matrix", fontsize=14, pad=10)

# Show in Streamlit
st.pyplot(fig)

# Classification report
report = classification_report(y_true, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

st.dataframe(report_df.style.format({"precision": "{:.2f}", "recall": "{:.2f}", "f1-score": "{:.2f}", "support": "{:.0f}"}))

st.markdown("""
---

### How the Model Works
- The Random Forest algorithm builds **multiple decision trees** during training.
- Each tree votes for a classification, and the majority vote determines the final prediction.
- This ensemble method helps reduce overfitting and improves generalization.
- Feature importance is computed by measuring how much each feature reduces uncertainty (impurity) across all trees.

---

### Next Steps
- Continue collecting more diverse data to improve model robustness.
- Explore tuning hyperparameters for better accuracy.
- Integrate model explainability tools (like SHAP or LIME) to interpret individual predictions.

---

Thank you for exploring our Driving Qualification Advisor model! Feel free to reach out with any questions or feedback.
""")
