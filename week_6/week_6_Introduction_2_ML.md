```markdown
# CETM313 - Workshop Week 06-4 Solutions

This document provides solutions and explanations for the exercises and questions from the **CETM313 - Workshop Week 06-4** on Machine Learning and Linear Regression.

---

## **Exercise 1: Answer the quiz available via Canvas**

**Solution:**  
The quiz is hosted on Canvas, so you need to log in to your Canvas account and complete the quiz there. The quiz will likely cover topics related to machine learning, supervised learning, and linear regression.

---

## **Exercise 2: Install the required libraries and their dependencies**

**Solution:**  
Run the following commands in your Python environment (e.g., Jupyter Notebook) to install the necessary libraries:

```python
!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install scikit-learn
```

After installation, restart the kernel to ensure the libraries are loaded correctly.

---

## **Exercise 3: Download and extract the dataset**

**Solution:**  
1. Go to the UCI Machine Learning Repository link provided: [Student Performance Dataset](https://doi.org/10.24432/C5TG7T).
2. Download the dataset in ZIP format.
3. Extract the files from the ZIP folder.
4. Inside the extracted folder, you will find another ZIP file named `student`. Extract this as well.
5. Copy the `student-mat.csv` file to the same directory as your Jupyter Notebook.

---

## **Exercise 4: Open the file using MS Excel to check its content**

**Solution:**  
1. Open the `student-mat.csv` file in MS Excel.
2. Review the columns and data to understand the structure of the dataset.

---

## **Exercise 5: Open the dataset using Pandas**

**Solution:**  
Use the following code to open the dataset using Pandas:

```python
import pandas as pd

# Define the file name
file_name = 'student-mat.csv'

# Read the CSV file
df = pd.read_csv(file_name, sep=';')

# Display the first 5 rows
display(df.head())
```

---

## **Exercise 6: Display basic information about the dataset**

**Solution:**  
Use the following code to display basic information about the dataset:

```python
# Display the shape of the DataFrame
print("Shape of the DataFrame:")
print(df.shape)

# Display the columns in the DataFrame
print("\nColumns in the DataFrame:")
print(df.columns)
```

---

## **Exercise 7: Display summary statistics of numerical columns**

**Solution:**  
Use the following code to display summary statistics:

```python
# Display summary statistics
print("\nSummary Statistics:")
display(df.describe())
```

---

## **Exercise 8: Check for missing data**

**Solution:**  
Use the following code to check for missing values:

```python
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
```

---

## **Exercise 9: Check for duplicated rows**

**Solution:**  
Use the following code to check for duplicated rows:

```python
# Check for duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
```

---

## **Exercise 10: Check for column data types**

**Solution:**  
Use the following code to check the data types of the columns:

```python
# Display data types of the columns
print("\nData types of the columns:")
print(df.dtypes)
```

---

## **Exercise 11: Create a correlation matrix**

**Solution:**  
Use the following code to create a correlation matrix and visualize it using a heatmap:

```python
import matplotlib.pyplot as plt

# Select only numerical columns
numerical_columns = df.select_dtypes(include=['int64', 'float64'])

# Calculate correlations
correlations = numerical_columns.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
plt.imshow(correlations, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlations)), correlations.columns, rotation=90)
plt.yticks(range(len(correlations)), correlations.columns)
plt.title('Correlation Heatmap of Student Performance Dataset')
plt.show()
```

---

## **Exercise 12: Generate value counts for categorical variables**

**Solution:**  
Use the following code to generate value counts for categorical variables:

```python
# Value counts for categorical variables
print("\nValue Counts for Categorical Variables:")
print(df['sex'].value_counts())
print(df['address'].value_counts())
```

---

## **Exercise 13: Visualize data using matplotlib**

**Solution:**  
Use the following code to create a histogram of the `age` column:

```python
import matplotlib.pyplot as plt

# Histogram of Age
plt.figure(figsize=(8, 6))
plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
```

---

## **Exercise 14: Build a linear regression model**

**Solution:**  
Use the following code to build a linear regression model:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Select feature and target variables
X = df[['G1']]  # Feature variable
y = df['G3']    # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the target values
y_pred = model.predict(X_test)
```

---

## **Exercise 15: Measure model performance**

**Solution:**  
Use the following code to calculate the Mean Absolute Error, Mean Squared Error, and R-squared:

```python
# Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print("R-squared:", r2)
```

---

## **Exercise 16: Visualize the regression line**

**Solution:**  
Use the following code to visualize the regression line:

```python
# Plot the data points and regression line
plt.scatter(X_test, y_test, color='black', label='Actual data')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regression line')
plt.title('Single Variable Linear Regression')
plt.xlabel('First Test Grade (G1)')
plt.ylabel('Final Grade (G3)')
plt.legend()
plt.show()
```

---

## **Exercise 17: Try 3 different independent variables**

**Solution:**  
Repeat the process in Exercise 14-16 using different independent variables (e.g., `G2`, `studytime`, `failures`). Compare the results and determine which variable provides the best prediction.

---

## **Exercise 18: Use multiple features for prediction**

**Solution:**  
Use the following code to redefine the feature variables and train the model with multiple features:

```python
# Feature variables
X = df[['G1', 'G2', 'age', 'traveltime', 'studytime', 'failures']]

# Split the data and train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared:", r2)
```

---

## **Exercise 19: Find another dataset and repeat the steps**

**Solution:**  
1. Go to a dataset hosting website like [Kaggle](https://www.kaggle.com/) or [UCI Machine Learning Repository](https://archive.ics.uci.edu/).
2. Download a dataset of your choice.
3. Repeat all the steps from Exercise 3 to Exercise 18 on the new dataset.

---

## **Upload your notebook to your ePortfolio**

Make sure to upload your completed Jupyter Notebook with the solutions to your ePortfolio.

---
