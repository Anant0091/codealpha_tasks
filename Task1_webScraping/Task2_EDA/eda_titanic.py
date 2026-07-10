# Task 2: Exploratory Data Analysis (EDA)

**Project:** Titanic Dataset Analysis

**Description:**  
Titanic dataset ka EDA kiya - survival rate, age distribution, class-wise analysis etc.

**Technologies Used:**  
- Pandas  
- NumPy  
- Matplotlib & Seaborn

**Files:**
- `eda_titanic.ipynb` (Jupyter Notebook)
- `titanic.csv` (Dataset)
  # Missing Values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Statistical Summary
print("\n=== Statistical Summary ===")
print(df.describe())
  # Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
  # Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),
            annot=True,
            cmap="coolwarm",
            fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
  # Task 2: Exploratory Data Analysis (EDA) - Titanic Dataset
# CodeAlpha Data Analyst Internship

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== Titanic EDA Started ===\n")

# Load the dataset (aapko titanic.csv upload karna hoga)
df = pd.read_csv('titanic.csv')

# Basic Information
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing Values:\n", df.isnull().sum())

# Survival Analysis
print("\nSurvival Rate:")
print(df['Survived'].value_counts(normalize=True) * 100)

# Visualizations
plt.figure(figsize=(15, 10))

# 1. Survival by Gender
plt.subplot(2, 2, 1)
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title('Survival by Gender')

# 2. Survival by Class
plt.subplot(2, 2, 2)
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title('Survival by Passenger Class')

# 3. Age Distribution
plt.subplot(2, 2, 3)
sns.histplot(data=df, x='Age', kde=True)
plt.title('Age Distribution')

# 4. Fare vs Survival
plt.subplot(2, 2, 4)
sns.boxplot(data=df, x='Survived', y='Fare')
plt.title('Fare Distribution by Survival')

plt.tight_layout()
plt.savefig('eda_visualizations.png')
plt.show()

print("\n✅ EDA Completed Successfully!")
print("Visualizations saved as 'eda_visualizations.png'")
