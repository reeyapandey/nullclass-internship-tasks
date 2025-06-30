
# 🎯 NULLCLASS Internship Tasks – Reeya Pandey

### 📅 Internship Duration:
30 May 2025 – 30 June 2025

---

## 📁 Project Overview

This repository contains the implementation of all 3 internship tasks assigned by **NULLCLASS** as part of the AI/ML internship program. It includes real-time applications of CNNs in age, gender, emotion, and nationality prediction with GUI and logging support.

---

## ✅ Task Breakdown

### 🔹 Task 1: Activation Map Visualization
- Visualizes intermediate layer outputs from a CNN to interpret learned features.
- Use Jupyter Notebook to run and view maps.

### 🔹 Task 2: Senior Citizen Detection (Webcam
- Detects age/gender in live webcam feed using OpenCV.
- Logs entries of individuals aged 60+ into a CSV file with timestamp.

### 🔹 Task 3: Nationality, Emotion, and Conditional Prediction
- Streamlit app to predict nationality, emotion, age, and dress color conditionally:
  - Indian: age, emotion, dress color
  - USA: age, emotion
  - African: emotion, dress color
  - Others: nationality, emotion
## ✅ Key Components

### 🧠 Core Model
- **Model File**: `Age_Sex_Detection.h5`
- A CNN-based dual-output model:
  - **Gender**: Binary classification (Sigmoid)
  - **Age**: Regression

---

## 🔬 Scripts and Their Purpose

| **Filename** | **Purpose** |
|--------------|-------------|
| `check_age_classification_accuracy.py` | Tests the accuracy of the model's age predictions |
| `check_gender_accuracy.py` | Evaluates gender classification accuracy |
| `check_gender_neutral_accuracy.py` | Evaluates accuracy of gender-neutral models |
| `club_age_nd_gender.py` | Merges predictions for both age and gender |
| `create_distributed_male_train_data.py` | Prepares balanced male training data |
| `create_gender_based_train_data.py` | Separates and creates gender-specific training sets |
| `create_gender_neutral_data.py` | Prepares dataset for gender-neutral model training |
| `create_gender_test_based_on_predictions.py` | Tests gender prediction on a generated test set |
| `create_train_val_test.py` | Splits the dataset into training, validation, and test sets |
| `data_stats.py` | Outputs dataset statistics like class distribution |
| `equalize_data_distributed_per_age_group_approach2.py` | Balances the data across age groups |
| `extract_data_genderwise.py` | Extracts and separates data based on gender |
| `subject_exclusive_chunking_approach3.py` | Splits data such that subjects are exclusive to each set |
| `test.py` | General testing script for inference and model behavior |
| `test_accuracy.py` | Evaluates and logs overall model performance |
| `test_accuracy_log.txt` | Output log of test metrics |
| `test_age_predictions.py` | Tests model predictions for age |
| `test_gender_neutral.py` | Tests gender-neutral model accuracy |
| `test_gender_neutral_for_female.py` | Gender-neutral testing focused on female data |
| `train_and_test_gender.py` | Trains and evaluates the gender model |
| `train_n_test_female_model.py` | Trains and tests models using female-only data |
| `train_n_test_gender_neutral_age.py` | Trains model on gender-neutral data for age prediction |
| `train_n_test_male_model.py` | Trains and tests models using male-only data |

---

## 📊 How to Run

### 🔹 Step 1: Install Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
🔹 Step 2: Model Training (Example)
bash
Copy
Edit
python train_n_test_gender_neutral_age.py
🔹 Step 3: Model Evaluation
bash
Copy
Edit
python test_accuracy.py
🔹 Step 4: Custom Testing
Use any of the test scripts depending on your evaluation goals:

bash
Copy
Edit
python test_gender_neutral.py
python check_age_classification_accuracy.py
python check_gender_accuracy.py
💡 Model Insights
The model was trained using gender-separated and combined datasets.

CNNs were built and tested with subject-exclusive splitting to reduce bias.

Accuracy results are logged in test_accuracy_log.txt.



