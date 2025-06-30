
# 🎯 NULLCLASS Internship Tasks – Reeya Pandey

### 📅 Internship Duration:
30 May 2025 – 30 June 2025

---

## 📁 Project Overview

This repository contains the implementation of all 3 internship tasks assigned by **NULLCLASS** as part of the AI/ML internship program. It includes real-time applications of CNNs in age, gender, emotion, and nationality prediction with GUI and logging support.

---

## ✅ Task Breakdown

### 🔹 Task 1: Activation Map Visualization
- File: `activation_maps.ipynb`
- Visualizes intermediate layer outputs from a CNN to interpret learned features.
- Use Jupyter Notebook to run and view maps.

### 🔹 Task 2: Senior Citizen Detection (Webcam)
- Files: `senior_citizen_detection.py`, `senior_citizen_log.csv`
- Detects age/gender in live webcam feed using OpenCV.
- Logs entries of individuals aged 60+ into a CSV file with timestamp.

### 🔹 Task 3: Nationality, Emotion, and Conditional Prediction
- File: `nationality_detection_app.py`
- Streamlit app to predict nationality, emotion, age, and dress color conditionally:
  - Indian: age, emotion, dress color
  - USA: age, emotion
  - African: emotion, dress color
  - Others: nationality, emotion

---

## 💾 Model Info

- Model Name: `Age_Sex_Detection.h5`
- Architecture: CNN with dual-output (gender: sigmoid, age: regression)
- Accuracy: 70%+ on test dataset

📥 [Download model weights (.h5)](https://github.com/reeyapandey/nullclass-internship-tasks/raw/main/Age_Sex_Detection.h5)

---

## 🧰 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Task 2 (Webcam + CSV Logging):
```bash
python senior_citizen_detection.py
```

### Task 3 (Streamlit GUI):
```bash
streamlit run nationality_detection_app.py
```

---

## 📄 Report

Final internship report: `internship_report_template.docx`
➡️ Rename it to `Reeya_Pandey_Internship_Report.docx` when finalized.

---
