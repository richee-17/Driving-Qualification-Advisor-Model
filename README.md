
# 🚗 Driving Qualification Advisor

This is a **Streamlit-based web application** that predicts whether a person is **qualified** to drive based on various demographic and performance features. The prediction is made using a trained **Random Forest Classifier**, and users can download a **personalized PDF report** of their prediction results.

---

## 📌 Features

- **Qualification Prediction** using a trained ML model  
-  **Visual breakdown** of user inputs  
-  **PDF Report Download** with prediction and scores  
-  **Model Insights**: Feature importance & evaluation metrics  
-  **Dataset Visualization**: Explore trends by gender, age, race, training, and more  

---

## 🧪 Try It Yourself

Users can:
- Enter demographic & driving skill data  
- Predict whether they're qualified  
- Visualize all input scores in a graph  
- Download and print a detailed PDF report  

---

## 🛠️ Technologies Used

- Python 3.11+  
- Streamlit  
- scikit-learn  
- pandas & numpy  
- matplotlib & seaborn  
- fpdf (for PDF export)  

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/driving-qualification-advisor.git
cd driving-qualification-advisor
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run Home.py
```

---

## 📂 Project Structure

```
driving_qualification_advisor/
|
├── Home.py
├── requirements.txt
├── README.md
├── driving_model.pkl
├── Drivers License Data.csv
├── pdf_generator.py
|
└── pages/
    ├── Try_it_Yourself.py
    ├── About_Model.py
    ├── Dataset_Insights.py
    └── Contact.py
```

---

## 📨 Feedback & Contributions

Feel free to fork this repository, open issues, or contribute via pull requests.

---
