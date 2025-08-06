# 🧠 Logistic Regression Classification Model

A machine learning classification project using Logistic Regression that achieves **98.82% accuracy on training data** and **98.24% on testing data** — demonstrating excellent generalization without overfitting.

---

## 📌 Project Overview

This project involves building and evaluating a Logistic Regression model on a labeled dataset to predict a target variable. The goal was to achieve high performance while maintaining generalization between training and testing datasets.

---

## 📊 Dataset

- **Format**: Structured CSV
- **Target variable**: `y` 
- **Features**: Multiple numerical features
- **Preprocessing**:
  - Missing value handling
  - Feature scaling (`StandardScaler`)
  - Train-test split 

---

## ⚙️ Technologies Used

- Python 3.13
- NumPy
- Pandas
- scikit-learn (`LogisticRegression`, `StandardScaler`, `train_test_split`)
- Jupyter Notebook

---


## 🔍 Model Details

- **Algorithm**: Logistic Regression
- **Scaler**: StandardScaler
- **Hyperparameters**:
  - `random_state=42` (for reproducibility)

---

## 📈 Results

| Metric         | Score     |
|----------------|-----------|
| Training Accuracy | 98.82% |
| Testing Accuracy  | 98.24% |
| Overfitting Gap   | ~0.58% (Very Low ✅) |

➡️ The model is well-fitted and generalizes effectively.


## How to run:

1. Clone the repo:

   git clone https://github.com/tanyachauhan084/<your-repo-name>.git
   cd <your-repo-name>

2. Install dependencies:

   pip install -r requirements.txt

3. Run the notebook 


## Author
