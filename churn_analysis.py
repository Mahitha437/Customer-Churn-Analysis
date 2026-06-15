import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())
print("\nData Types:")
print(df.dtypes)
# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Check missing values again
print("\nMissing Values After Conversion:")
print(df.isnull().sum())
# Remove rows with missing values
df.dropna(inplace=True)

print("\nShape After Removing Missing Values:")
print(df.shape)
# Churn Distribution
plt.figure(figsize=(6,5))
sns.countplot(x='Churn', data=df)

plt.title('Customer Churn Distribution')
plt.xlabel('Churn')
plt.ylabel('Number of Customers')

plt.savefig('Visualizations/churn_distribution.png')
#plt.show()
# Gender vs Churn
plt.figure(figsize=(7,5))
sns.countplot(x='gender', hue='Churn', data=df)

plt.title('Gender vs Churn')
plt.xlabel('Gender')
plt.ylabel('Number of Customers')

plt.savefig('Visualizations/gender_vs_churn.png')
#plt.show()
# Contract vs Churn
plt.figure(figsize=(8,5))
sns.countplot(x='Contract', hue='Churn', data=df)

plt.title('Contract vs Churn')
plt.xlabel('Contract Type')
plt.ylabel('Number of Customers')

plt.savefig('Visualizations/contract_vs_churn.png')
#plt.show()
# Internet Service vs Churn
plt.figure(figsize=(8,5))
sns.countplot(x='InternetService', hue='Churn', data=df)

plt.title('Internet Service vs Churn')
plt.xlabel('Internet Service')
plt.ylabel('Number of Customers')

plt.savefig('Visualizations/internet_service_vs_churn.png')
# plt.show()
# Monthly Charges Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['MonthlyCharges'], bins=30, kde=True)

plt.title('Monthly Charges Distribution')
plt.xlabel('Monthly Charges')
plt.ylabel('Number of Customers')

plt.savefig('Visualizations/monthly_charges_distribution.png')
# plt.show()