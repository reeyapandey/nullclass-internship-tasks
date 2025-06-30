# 🎯 NULLCLASS Internship Project – Reeya Pandey

## 📅 Internship Duration
**30 May 2025 – 30 June 2025**

---

## 📁 Project Overview

This repository contains all the code, models, and scripts developed during my AI/ML internship at **NULLCLASS**. The project focuses on building Convolutional Neural Networks (CNNs) to perform **age and gender prediction**, with experiments around gender neutrality, subject-exclusive data splitting, and data balancing techniques.

---

## ✅ Key Components

### 🧠 Core Model
- **Model Name**: `Age_Sex_Detection.h5`
- **Architecture**: CNN with dual-output
  - Gender: Binary classification (sigmoid)
  - Age: Regression
- **Accuracy**: 70%+ on test data

---

## 🔬 Scripts and Usage

### 📊 Evaluation Scripts
- `check_age_classification_accuracy.py`: Evaluates age prediction accuracy
- `check_gender_accuracy.py`: Evaluates gender prediction accuracy
- `check_gender_neutral_accuracy.py`: Evaluates accuracy of gender-neutral model
- `test_accuracy.py`: Logs and prints final model accuracy
- `test_accuracy_log.txt`: Contains the output logs from test evaluations
- `test_age_predictions.py`: Runs prediction script for age estimation
- `test_gender_neutral.py`: Tests gender-neutral model on test data
- `test_gender_neutral_for_female.py`: Gender-neutral model tested on female data
- `test.py`: General testing script

### 🧪 Training Scripts
- `train_and_test_gender.py`: Trains and tests model for gender
- `train_n_test_female_model.py`: Trains and tests model on female-only data
- `train_n_test_male_model.py`: Trains and tests model on male-only data
- `train_n_test_gender_neutral_age.py`: Trains model on gender-neutral age data

### 🏗️ Data Preparation
- `create_train_val_test.py`: Splits the dataset into train/val/test sets
- `create_gender_based_train_data.py`: Filters and creates gender-based training data
- `create_distributed_male_train_data.py`: Prepares male-distributed training set
- `create_gender_neutral_data.py`: Prepares dataset excluding gender labels
- `create_gender_test_based_on_predictions.py`: Creates test data using predictions
- `equalize_data_distributed_per_age_group_approach2.py`: Balances dataset across age groups
- `extract_data_genderwise.py`: Splits dataset by gender
- `subject_exclusive_chunking_approach3.py`: Ensures subject-exclusivity across dataset
- `data_stats.py`: Prints statistics about the dataset
- `club_age_nd_gender.py`: Combines age and gender predictions

---

## 🚀 How to Run

### 🔹 Step 1: Install Dependencies
Install all necessary libraries using:
```bash
pip install -r requirements.txt

### 🔹 Step 2: Train a Model
bash
Copy
Edit
python train_n_test_gender_neutral_age.py

### 🔹 Step 3: Evaluate Model Accuracy
bash
Copy
Edit
python test_accuracy.py

### 🔹 Step 4: Test Age/Gender Predictions
bash
Copy
Edit
python check_age_classification_accuracy.py
python check_gender_accuracy.py

