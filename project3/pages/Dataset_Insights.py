import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="📊 Dataset Insights", layout="centered")
st.title("📊 Dataset Insights")

# Load data
df = pd.read_csv("Drivers License Data.csv")

# Convert 'Qualified' from 0/1 to labels
if df["Qualified"].dtype != "object":
    df["Qualified"] = df["Qualified"].map({1: "Qualified", 0: "Not Qualified"})

sns.set_style("whitegrid")
pastel_palette = sns.color_palette("pastel")

# Helper function for consistent sizing
def small_fig():
    return plt.subplots(figsize=(6, 4))

# --- 1. Qualified vs Not Qualified 
st.subheader(" Qualification Distribution")
qualified_counts = df["Qualified"].value_counts()
fig1, ax1 = small_fig()
ax1.pie(qualified_counts, labels=qualified_counts.index, autopct="%1.1f%%", colors=pastel_palette)
ax1.set_title("Qualified vs Not Qualified", fontsize=13)
st.pyplot(fig1)

# --- 2 Qualification by Gender
st.subheader(" Gender-wise Qualification")
fig2, ax2 = small_fig()
sns.countplot(data=df, x="Gender", hue="Qualified", palette="pastel", ax=ax2)
ax2.set_title("Qualification by Gender", fontsize=13)
st.pyplot(fig2)

# --- 3. Age vs Qualified 
st.subheader("📈 Age Group vs Qualification (Violin Plot)")
fig3, ax3 = small_fig()
sns.violinplot(data=df, x="Age Group", y="Speed Control", hue="Gender", palette="pastel", ax=ax3, split=True)
ax3.set_title("Speed Control across Age Groups (by Gender)", fontsize=13)
st.pyplot(fig3)

# --- 4. Age vs Confidence 
st.subheader(" Confidence vs Age Group (by Gender)")
fig4, ax4 = small_fig()
sns.stripplot(data=df, x="Age Group", y="Confidence", hue="Gender", palette="pastel", dodge=True, ax=ax4)
ax4.set_title("Confidence by Age Group", fontsize=13)
st.pyplot(fig4)

# --- 5. Race vs Confidenc
st.subheader("Race vs Confidence")
fig5, ax5 = small_fig()
sns.violinplot(data=df, x="Race", y="Confidence", hue="Gender", palette="pastel", split=True, ax=ax5)
ax5.set_title("Confidence across Races", fontsize=13)
plt.xticks(rotation=30)
st.pyplot(fig5)

# --- 6.Training vs Confidenc
st.subheader("🎓 Training vs Confidence (by Gender)")
fig6, ax6 = small_fig()
sns.stripplot(data=df, x="Training", y="Confidence", hue="Gender", dodge=True, palette="pastel", ax=ax6)
ax6.set_title("Confidence by Training Level", fontsize=13)
st.pyplot(fig6)

# --- 7. Total Qualified vs Not Qualified 
st.subheader("📋 Total Qualification Count")
fig7, ax7 = small_fig()
sns.countplot(data=df, x="Qualified", hue="Gender", palette="pastel", ax=ax7)
ax7.set_title("Overall Qualification Status", fontsize=13)
st.pyplot(fig7)

# --- 8. Speed Score vs Qualification 
st.subheader("🚦 Speed Control vs Qualification")
fig8, ax8 = small_fig()
sns.violinplot(data=df, x="Qualified", y="Speed Control", hue="Gender", palette="pastel", split=True, ax=ax8)
ax8.set_title("Speed Control Distribution by Qualification", fontsize=13)
st.pyplot(fig8)

# --- 9. Speed Score vs Training  
st.subheader(" Speed Score vs Training (Line Plot)")
fig9, ax9 = small_fig()
sns.lineplot(data=df, x="Training", y="Speed Control", hue="Gender", marker='o', palette="pastel", ax=ax9)
ax9.set_title("Speed Score Trend by Training", fontsize=13)
st.pyplot(fig9)
