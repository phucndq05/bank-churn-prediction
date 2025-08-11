# Bank Customer Churn Prediction & Web App Demo

A **machine learning project** to analyze customer data and predict churn.  
The goal is to identify key factors that lead to customer attrition, train a reliable classification model, and deploy the best-performing model in an interactive **Flask web application**.

---

## 📊 Dataset

The dataset used is the **Bank Customer Churn Prediction** dataset from Kaggle, which has a high usability score.  
- **Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction)

---

## 🚀 Key Features

- **Comprehensive EDA:** In-depth exploratory data analysis with advanced visualizations (KDE plots, choropleth maps) to uncover business insights.
- **Model Benchmarking:** Trains and compares multiple models (Logistic Regression, Random Forest) to select the best performer.
- **Model Persistence:** Saves the trained model and data scaler using `joblib` for deployment.
- **Interactive Web Interface:** A Flask-based app for live predictions on new customer data.

---

## 🛠 Tech Stack

- **Language:** Python
- **Libraries:**
  - **Data Manipulation:** Pandas, NumPy
  - **Visualization:** Matplotlib, Seaborn, Plotly
  - **Machine Learning:** Scikit-learn
  - **Web Framework:** Flask
  - **Model Persistence:** Joblib

---

## 📂 Project Workflow

1. **Exploratory Data Analysis (EDA):** Investigate the dataset to find initial patterns and insights.
2. **Data Preprocessing:** Clean the data, handle categorical features, and scale numerical features.
3. **Model Training:** Train and compare multiple classification models (Logistic Regression, Random Forest).
4. **Model Evaluation:** Evaluate performance using metrics like Accuracy, Precision, Recall, and F1-Score.
5. **Deployment:** Serve the best-performing model via a Flask web application.

---

## 🏁 Getting Started

### 1️⃣ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/phucndq05/bank-churn-prediction.git
   cd bank-churn-prediction
   ```
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

### 2️⃣ Run Data Analysis

To explore the EDA and model training process, open the Jupyter Notebook:
```bash
jupyter notebook bank_churn_analysis.ipynb
```

---

### 3️⃣ Launch Web Application

Run the Flask app:
```bash
python3 app.py
```
Then open your browser and visit: **http://127.0.0.1:5000**

---

## 📂 Project Structure
```
bank-churn-prediction/
├── deployment/
│   ├── model.pkl
│   └── scaler.pkl
├── templates/
│   ├── index.html
│   └── result.html
├── data/
│   └── Churn_Modelling.csv
├── app.py
├── bank_churn_analysis.ipynb
├── requirements.txt
└── README.md
```
