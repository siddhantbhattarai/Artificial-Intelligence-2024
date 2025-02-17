# CET313 AI Lab Workshop 7: Machine Learning Classifiers – Solutions

This document outlines the step-by-step solutions for the workshop exercises. The exercises focus on applying machine learning classifiers to the Breast Cancer dataset (and later, other datasets such as Iris and Wine) from the UCI repository using Python. Follow along with the code examples below.

---

## Exercise 1: Quiz

- **Task:** Answer the quiz available via Canvas.
- **Solution:**  
  Complete the quiz on Canvas. (No code is required.)

---

## Exercise 2: Install the Required Libraries

- **Task:** Install Pandas, NumPy, Matplotlib, and scikit-learn.
- **Solution:**  
  Run the following installation commands in your terminal or a notebook cell:
  
  ```bash
  pip install pandas
  pip install numpy
  pip install matplotlib
  pip install scikit-learn
  ```

---

## Exercise 3: Problem Determination and Dataset Selection

- **Task:** Determine a problem and select a dataset. In this example, we use the Breast Cancer dataset.
- **Solution:**  
  We will use the Breast Cancer dataset for classification. This dataset is available from the UCI Machine Learning Repository and is also accessible via the scikit-learn library.

---

## Exercise 4: Import the Relevant Libraries

- **Task:** Import the necessary Python libraries.
- **Solution:**

  ```python
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import StandardScaler
  from sklearn.linear_model import LogisticRegression
  from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, roc_auc_score
  from sklearn.datasets import load_breast_cancer
  ```

---

## Exercise 5: Load the Dataset

- **Task:** Load the Breast Cancer dataset.
- **Solution:**

  ```python
  # Load the Breast Cancer dataset from sklearn
  data = load_breast_cancer()
  X = data.data
  y = data.target
  feature_names = data.feature_names
  target_names = data.target_names
  ```

---

## Exercise 6: Analyze the Dataset

- **Task:** Assess the dataset by visualizing the class distribution.
- **Solution:**

  ```python
  # Visualizing the classes distribution
  plt.figure(figsize=(6, 4))
  plt.bar(target_names, np.bincount(y))
  plt.xlabel('Class')
  plt.ylabel('Count')
  plt.title('Class Distribution')
  plt.show()
  ```

- *Extra Task:* Read about the effects of imbalanced data on models (Resource: Introduction to Machine Learning with Python on O'Reilly).

---

## Exercise 7: Split the Dataset into Training and Testing Sets

- **Task:** Create training and testing sets.
- **Solution:**

  ```python
  # Splitting the dataset into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```

- *Extra Task:* Research overfitting (Resources: IBM’s explanation on overfitting and related O'Reilly chapters).

---

## Exercise 8: Feature Scaling

- **Task:** Scale the dataset features using StandardScaler.
- **Solution:**

  ```python
  # Feature scaling
  scaler = StandardScaler()
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.transform(X_test)
  ```

- *Extra Task:* Read about scaling in the preprocessing chapter of Introduction to Machine Learning with Python.

---

## Exercise 9: Train a Logistic Regression Model

- **Task:** Train a logistic regression classifier on the training data.
- **Solution:**

  ```python
  # Fitting logistic regression to the training set
  classifier = LogisticRegression(random_state=0)
  classifier.fit(X_train, y_train)
  ```

---

## Exercise 10: Make Predictions

- **Task:** Predict the class labels of the test set.
- **Solution:**

  ```python
  # Predicting the test set results
  y_pred = classifier.predict(X_test)
  ```

---

## Exercise 11: Evaluate the Model

- **Task:** Evaluate the classifier using accuracy, classification report, and confusion matrix.
- **Solution:**

  ```python
  # Evaluating the model
  print("Accuracy:", accuracy_score(y_test, y_pred))
  print("\nClassification Report:\n", classification_report(y_test, y_pred))
  print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
  ```

- *Reference:* Techniques based on Introduction to Machine Learning with Python.

---

## Exercise 12: Visualize the Confusion Matrix

- **Task:** Plot the confusion matrix.
- **Solution:**

  ```python
  # Plotting the confusion matrix
  conf_matrix = confusion_matrix(y_test, y_pred)
  plt.imshow(conf_matrix, cmap='Blues', interpolation='nearest')
  plt.title('Confusion Matrix')
  plt.colorbar()
  tick_marks = np.arange(len(target_names))
  plt.xticks(tick_marks, target_names)
  plt.yticks(tick_marks, target_names)
  plt.xlabel('Predicted')
  plt.ylabel('Actual')
  plt.show()
  ```

---

## Exercise 13: Plot the ROC Curve

- **Task:** Plot the Receiver Operating Characteristic (ROC) curve.
- **Solution:**

  ```python
  # Plotting the ROC curve
  y_pred_proba = classifier.predict_proba(X_test)[:, 1]
  fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
  plt.plot(fpr, tpr, label='ROC Curve')
  plt.plot([0, 1], [0, 1], 'k--')
  plt.xlabel('False Positive Rate')
  plt.ylabel('True Positive Rate')
  plt.title('Receiver Operating Characteristic (ROC) Curve')
  plt.legend(loc='lower right')
  plt.show()
  ```

---

## Exercise 14: Visualize Feature Importance

- **Task:** Visualize the importance of features by plotting the coefficients of the logistic regression model.
- **Solution:**

  ```python
  # Plotting feature importance for Logistic Regression
  coefficients = classifier.coef_[0]
  sorted_indices = np.argsort(coefficients)
  plt.figure(figsize=(10, 8))
  plt.barh(range(len(coefficients)), coefficients[sorted_indices], align='center')
  plt.yticks(range(len(coefficients)), feature_names[sorted_indices])
  plt.title('Feature Importance (Coefficient Values)')
  plt.xlabel('Coefficient')
  plt.ylabel('Feature')
  plt.show()
  ```

---

## Exercise 15: Compare with Other Classification Algorithms

- **Task:** Train and compare SVM and Decision Tree classifiers.
- **Solution:**

  ```python
  from sklearn.svm import SVC
  from sklearn.tree import DecisionTreeClassifier
  
  # SVM classifier
  svm_classifier = SVC(probability=True, random_state=0)
  svm_classifier.fit(X_train, y_train)
  y_pred_svm = svm_classifier.predict(X_test)
  print("SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
  
  # Decision Tree classifier
  tree_classifier = DecisionTreeClassifier(random_state=0)
  tree_classifier.fit(X_train, y_train)
  y_pred_tree = tree_classifier.predict(X_test)
  print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred_tree))
  ```

- *Resources:* Refer to the scikit-learn documentation for [Decision Trees](https://scikit-learn.org/stable/modules/tree.html) and [SVM](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html).

---

## Exercise 16: Test on the Iris Dataset

- **Task:** Apply the pipeline to a different dataset, the Iris dataset.
- **Solution:**

  ```python
  from sklearn.datasets import load_iris
  
  # Loading the Iris dataset
  iris_data = load_iris()
  X_iris = iris_data.data
  y_iris = iris_data.target
  iris_feature_names = iris_data.feature_names
  iris_target_names = iris_data.target_names
  
  # Splitting the Iris dataset
  X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)
  
  # Scaling features
  X_train_iris = scaler.fit_transform(X_train_iris)
  X_test_iris = scaler.transform(X_test_iris)
  
  # Training a logistic regression model on the Iris dataset
  iris_classifier = LogisticRegression(random_state=0)
  iris_classifier.fit(X_train_iris, y_train_iris)
  y_pred_iris = iris_classifier.predict(X_test_iris)
  print("Iris Dataset Accuracy:", accuracy_score(y_test_iris, y_pred_iris))
  ```

---

## Exercise 17: Experiment with Another UCI Dataset

- **Task:** Choose any classification dataset from the UCI Machine Learning Repository and test the pipeline.
- **Solution:**  
  For example, here’s how to test the pipeline using the Wine dataset:

  ```python
  from sklearn.datasets import load_wine
  
  # Loading the Wine dataset (as an example)
  wine_data = load_wine()
  X_wine = wine_data.data
  y_wine = wine_data.target
  
  # Splitting the Wine dataset
  X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(X_wine, y_wine, test_size=0.2, random_state=42)
  
  # Scaling features
  X_train_wine = scaler.fit_transform(X_train_wine)
  X_test_wine = scaler.transform(X_test_wine)
  
  # Training a logistic regression model on the Wine dataset
  wine_classifier = LogisticRegression(random_state=0)
  wine_classifier.fit(X_train_wine, y_train_wine)
  y_pred_wine = wine_classifier.predict(X_test_wine)
  print("Wine Dataset Accuracy:", accuracy_score(y_test_wine, y_pred_wine))
  ```

  *Note:* You can choose any dataset from the UCI repository and apply a similar pipeline.

---

## Final Note

Make sure you upload your completed notebook with these solutions to your portfolio. Experiment further with other models and datasets to deepen your understanding.
