# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
# Dummy Data for Fee Income
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Total_Fee_Income": [100000, 120000, 115000, 130000, 125000, 140000]
}

# Allocate income to SBUs (Retail, Corporate, SME)
allocation_ratio = {"Retail": 0.5, "Corporate": 0.3, "SME": 0.2}

df = pd.DataFrame(data)
for sbu, ratio in allocation_ratio.items():
    df[sbu] = df["Total_Fee_Income"] * ratio

print("Fee Income Report by SBUs:")
print(df)

# Plotting SBU Allocation for the latest month
latest_month = df.iloc[-1]
labels = list(allocation_ratio.keys())
values = [latest_month[sbu] for sbu in labels]

plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'orange', 'lightgreen'])
plt.title(f"Fee Income Allocation for {latest_month['Month']}")
plt.show()

# Dummy Data for SBU-wise contribution
sbu_data = {
    "SBU": ["Retail", "Corporate", "SME"],
    "Amount (USD)": [500000, 150000, 50000]
}

# Extracting labels and values for the pie chart
labels = sbu_data["SBU"]
amounts = sbu_data["Amount (USD)"]

# Creating the Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(
    amounts, 
    labels=labels, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['skyblue', 'orange', 'lightgreen'],
    wedgeprops={'edgecolor': 'black'}
)
plt.title("SBU-wise Contribution", fontsize=16)
plt.show()

# Dummy Data for Advance Income Amortization
advance_income = 12000  # Advance income received upfront
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
amortization_rate = 2000  # Monthly amortization amount

amortization_schedule = {
    "Month": months,
    "Amortized_Income": [amortization_rate] * len(months),
    "Remaining_Advance": [advance_income - i * amortization_rate for i in range(len(months))]
}

df_amortization = pd.DataFrame(amortization_schedule)
print("Amortization Schedule:")
print(df_amortization)

# Plot Amortization over Time
plt.figure(figsize=(10, 5))
plt.plot(df_amortization["Month"], df_amortization["Remaining_Advance"], marker='o', label="Remaining Advance")
plt.bar(df_amortization["Month"], df_amortization["Amortized_Income"], alpha=0.7, label="Amortized Income")
plt.xlabel("Month")
plt.ylabel("Amount (USD)")
plt.title("Amortization & Remaining Advance Income")
plt.legend()
plt.show()

# Dummy Data for Budget vs Actuals
budget_data = {
    "SBU": ["Retail", "Corporate", "SME"],
    "Budget_Q1": [50000, 30000, 20000],
    "Actual_Q1": [48000, 32000, 19000]
}

df_budget = pd.DataFrame(budget_data)
df_budget["Variance"] = df_budget["Actual_Q1"] - df_budget["Budget_Q1"]

print("Budget vs Actuals:")
print(df_budget)

# Bar Chart for Budget vs Actuals
plt.figure(figsize=(10, 6))
x = df_budget["SBU"]
bar_width = 0.35
plt.bar(x, df_budget["Budget_Q1"], width=bar_width, label="Budget", color='skyblue')
plt.bar(x, df_budget["Actual_Q1"], width=bar_width, label="Actual", color='orange', alpha=0.7, bottom=df_budget["Budget_Q1"])
plt.xlabel("SBU")
plt.ylabel("Amount (USD)")
plt.title("Budget vs Actuals with Variance")
plt.legend()
plt.show()

# Dummy Data for Liabilities
liabilities_data = {
    "Account": ["L1", "L2", "L3", "L4", "L5"],
    "Days_Pending": [15, 45, 70, 10, 35],
    "Amount": [10000, 20000, 15000, 5000, 12000]
}

ageing_buckets = {
    "0-30 Days": (0, 30),
    "31-60 Days": (31, 60),
    "61+ Days": (61, float('inf'))
}

df_liabilities = pd.DataFrame(liabilities_data)
df_liabilities["Ageing_Bucket"] = df_liabilities["Days_Pending"].apply(
    lambda x: next(bucket for bucket, (low, high) in ageing_buckets.items() if low <= x <= high)
)

print("Liability Ageing Analysis:")
print(df_liabilities)

# Bar Chart for Ageing Buckets
ageing_summary = df_liabilities.groupby("Ageing_Bucket")["Amount"].sum()

plt.figure(figsize=(10, 6))
ageing_summary.plot(kind='bar', color='teal')
plt.xlabel("Ageing Bucket")
plt.ylabel("Amount (USD)")
plt.title("Liability Ageing Analysis")
plt.show()

# Dummy GL Data
gl_data = {
    "GL_Code": [101, 102, 103, 104, 105],
    "Description": ["Retail Income", "Corporate Expense", "SME Income", "Interest", None],
    "Amount": [50000, -30000, 20000, 10000, -5000]
}

df_gl = pd.DataFrame(gl_data)

# Check for Missing Descriptions
missing_descriptions = df_gl[df_gl["Description"].isnull()]
print("Missing GL Descriptions:")
print(missing_descriptions)

# Plot GL Balances
plt.figure(figsize=(10, 5))
plt.bar(df_gl["GL_Code"], df_gl["Amount"], color='purple', alpha=0.7)
plt.xlabel("GL Code")
plt.ylabel("Amount (USD)")
plt.title("GL Account Balances")
plt.show()

# Save Fee Income Report DataFrame
df.to_csv("fee_income_report.csv", index=False)

# Save Amortization Schedule DataFrame
df_amortization.to_csv("amortization_schedule.csv", index=False)

# Save Budget vs Actuals DataFrame
df_budget.to_csv("budget_vs_actuals.csv", index=False)

# Save Liability Ageing Analysis DataFrame
df_liabilities.to_csv("liability_ageing_analysis.csv", index=False)

# Save GL Data DataFrame
df_gl.to_csv("general_ledger.csv", index=False)

print("All DataFrames have been successfully saved as CSV files!")
