<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>NULLCLASS Internship Project – Reeya Pandey</title>
  <style>
    body {
      font-family: 'Times New Roman', serif;
      margin: 40px;
      background-color: #f4f4f4;
      color: #333;
      line-height: 1.6;
    }
    h1, h2, h3 {
      color: #1a1a1a;
    }
    code {
      background: #eee;
      padding: 2px 6px;
      border-radius: 4px;
    }
    pre {
      background: #eee;
      padding: 12px;
      border-radius: 4px;
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1em;
    }
    th, td {
      border: 1px solid #aaa;
      padding: 8px;
      text-align: left;
    }
    th {
      background: #ddd;
    }
  </style>
</head>
<body>

<h1>🎯 NULLCLASS Internship Project – Reeya Pandey</h1>

<h2>📅 Internship Duration</h2>
<p><strong>30 May 2025 – 30 June 2025</strong></p>

<hr />

<h2>📁 Project Overview</h2>
<p>
This repository showcases the work completed as part of the AI/ML internship at <strong>NULLCLASS</strong>. The focus of the project is on building and evaluating Convolutional Neural Networks (CNNs) for <strong>age and gender detection</strong>, with additional experiments for <strong>gender-neutral models</strong>, <strong>data balancing</strong>, and <strong>performance analysis</strong>.
</p>

<hr />

<h2>✅ Key Components</h2>

<h3>🧠 Core Model</h3>
<ul>
  <li><strong>Model File:</strong> <code>Age_Sex_Detection.h5</code></li>
  <li>A CNN-based dual-output model:
    <ul>
      <li><strong>Gender:</strong> Binary classification (Sigmoid)</li>
      <li><strong>Age:</strong> Regression</li>
    </ul>
  </li>
</ul>

<h3>🔬 Scripts and Their Purpose</h3>
<table>
  <thead>
    <tr>
      <th>Filename</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>check_age_classification_accuracy.py</td><td>Tests accuracy of the model's age predictions</td></tr>
    <tr><td>check_gender_accuracy.py</td><td>Evaluates gender classification accuracy</td></tr>
    <tr><td>check_gender_neutral_accuracy.py</td><td>Evaluates accuracy of gender-neutral models</td></tr>
    <tr><td>club_age_nd_gender.py</td><td>Merges predictions for both age and gender</td></tr>
    <tr><td>create_distributed_male_train_data.py</td><td>Prepares balanced male training data</td></tr>
    <tr><td>create_gender_based_train_data.py</td><td>Creates gender-specific training datasets</td></tr>
    <tr><td>create_gender_neutral_data.py</td><td>Prepares gender-neutral dataset</td></tr>
    <tr><td>create_gender_test_based_on_predictions.py</td><td>Tests predictions based on generated test set</td></tr>
    <tr><td>create_train_val_test.py</td><td>Splits dataset into training/validation/testing</td></tr>
    <tr><td>data_stats.py</td><td>Displays statistics about the dataset</td></tr>
    <tr><td>equalize_data_distributed_per_age_group_approach2.py</td><td>Balances dataset across age groups</td></tr>
    <tr><td>extract_data_genderwise.py</td><td>Separates dataset by gender</td></tr>
    <tr><td>subject_exclusive_chunking_approach3.py</td><td>Ensures subject exclusivity across sets</td></tr>
    <tr><td>test.py</td><td>General test script for prediction</td></tr>
    <tr><td>test_accuracy.py</td><td>Calculates and logs accuracy</td></tr>
    <tr><td>test_accuracy_log.txt</td><td>Log file with evaluation output</td></tr>
    <tr><td>test_age_predictions.py</td><td>Tests model predictions for age</td></tr>
    <tr><td>test_gender_neutral.py</td><td>Tests gender-neutral predictions</td></tr>
    <tr><td>test_gender_neutral_for_female.py</td><td>Tests on female-only gender-neutral data</td></tr>
    <tr><td>train_and_test_gender.py</td><td>Trains and evaluates gender classifier</td></tr>
    <tr><td>train_n_test_female_model.py</td><td>Trains and evaluates female-only models</td></tr>
    <tr><td>train_n_test_gender_neutral_age.py</td><td>Trains age model with gender-neutral data</td></tr>
    <tr><td>train_n_test_male_model.py</td><td>Trains and evaluates male-only models</td></tr>
  </tbody>
</table>

<hr />

<h2>📊 How to Run</h2>

<h3>🔹 Step 1: Install Requirements</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>🔹 Step 2: Train a Model (Example)</h3>
<pre><code>python train_n_test_gender_neutral_age.py</code></pre>

<h3>🔹 Step 3: Evaluate Model</h3>
<pre><code>python test_accuracy.py</code></pre>

<h3>🔹 Step 4: Run Custom Tests</h3>
<pre><code>python check_gender_accuracy.py
python check_age_classification_accuracy.py
python test_gender_neutral.py</code></pre>

<hr />

<h2>💡 Model Insights</h2>
<ul>
  <li>Tested both gender-specific and gender-neutral training strategies</li>
  <li>Subject-exclusive splits were used to reduce identity bias</li>
  <li>Accuracy logs available in <code>test_accuracy_log.txt</code></li>
</ul>

<hr />

<h2>📝 Report Submission</h2>
<ol>
  <li>Download <code>internship_report_template.docx</code></li>
  <li>Complete and rename it to: <strong>Reeya_Pandey_Internship_Report.docx</strong></li>
</ol>

<hr />

<h2>🙋 About the Intern</h2>
<ul>
  <li><strong>Name:</strong> Reeya Pandey</li>
  <li><strong>Role:</strong> AI/ML Intern</li>
  <li><strong>Focus Areas:</strong> Deep Learning, CNN, Bias Reduction, Gender Neutrality</li>
</ul>

<hr />

<h2>📌 Notes</h2>
<ul>
  <li>Models designed with fairness and inclusiveness in mind</li>
  <li>All scripts are modular for reproducibility</li>
  <li>Dataset pre-processing and augmentation included</li>
</ul>

<hr />

<p style="text-align:center;">© 2025 Reeya Pandey | NULLCLASS Internship Project</p>

</body>
</html>
