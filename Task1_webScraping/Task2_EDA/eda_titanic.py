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
  
