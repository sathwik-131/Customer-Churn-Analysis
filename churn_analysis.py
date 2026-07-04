import pandas as pd
import matplotlib.pyplot as plt

print("Program Started...")

try:
    df = pd.read_csv("customer_data.csv")
    print("File loaded successfully!\n")
except FileNotFoundError:
    print("Error: customer_data.csv file not found")
    exit()

print("CUSTOMER DATA")
print(df.head())

print("\nMISSING VALUES")
print(df.isnull().sum())


total_customers = len(df)
print("\nTotal Customers:", total_customers)


churn_customers = df["Churn"].sum()
print("Customers Left:", churn_customers)

churn_rate = (churn_customers / total_customers) * 100
print("Churn Rate:", churn_rate, "%")

print("\nAverage Monthly Usage")
print(df.groupby("Churn")["MonthlyUsage"].mean())

print("\nAverage Support Calls")
print(df.groupby("Churn")["SupportCalls"].mean())

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Analysis")
plt.xlabel("0 = Stayed | 1 = Left")
plt.ylabel("Number of Customers")
plt.show()

df.to_csv("churn_result.csv", index=False)

print("\nProject Completed Successfully!")