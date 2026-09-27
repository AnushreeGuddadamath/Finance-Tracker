import pandas as pd
import os

file_name = "finance_data.csv"

# Create CSV File
if not os.path.exists(file_name):
    df = pd.DataFrame(columns=["ID", "Type", "Category", "Amount", "Date"])
    df.to_csv(file_name, index=False)

# Add Transaction
def add_transaction():
    tid = input("Enter Transaction ID: ")
    ttype = input("Enter Type (Income/Expense): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date: ")

    data = pd.DataFrame({
        "ID": [tid],
        "Type": [ttype],
        "Category": [category],
        "Amount": [amount],
        "Date": [date]
    })

    data.to_csv(file_name, mode='a', header=False, index=False)

    print("✅ Transaction Added Successfully")

# View Transactions
def view_transactions():
    df = pd.read_csv(file_name)
    print(df)

# Financial Summary
def financial_summary():
    df = pd.read_csv(file_name)

    income = df[df['Type'] == "Income"]['Amount'].sum()
    expense = df[df['Type'] == "Expense"]['Amount'].sum()

    print("Total Income :", income)
    print("Total Expense:", expense)
    print("Balance      :", income - expense)

# Monthly Expense Analysis
def monthly_expense():
    df = pd.read_csv(file_name)

    expense = df[df['Type'] == "Expense"]['Amount'].sum()

    print("Monthly Expense:", expense)

# Highest Spending Category
def highest_spending():
    df = pd.read_csv(file_name)

    category = df.groupby('Category')['Amount'].sum().idxmax()

    print("Highest Spending Category:", category)

# Monthly Savings
def monthly_savings():
    df = pd.read_csv(file_name)

    income = df[df['Type'] == "Income"]['Amount'].sum()
    expense = df[df['Type'] == "Expense"]['Amount'].sum()

    print("Monthly Savings:", income - expense)

# Average Daily Spending
def average_spending():
    df = pd.read_csv(file_name)

    avg = df['Amount'].mean()

    print("Average Spending:", avg)

# Transaction Frequency
def transaction_frequency():
    df = pd.read_csv(file_name)

    print("Total Transactions:", len(df))

# Category-wise Spending Trend
def spending_trend():
    df = pd.read_csv(file_name)

    trend = df.groupby('Category')['Amount'].sum()

    print(trend)

# High Expense Detection
def high_expense():
    df = pd.read_csv(file_name)

    high = df[df['Amount'] > 1000]

    print(high)

# Income vs Expense Ratio
def income_expense_ratio():
    df = pd.read_csv(file_name)

    income = df[df['Type'] == "Income"]['Amount'].sum()
    expense = df[df['Type'] == "Expense"]['Amount'].sum()

    print("Ratio:", income / expense)

# Most Frequent Spending Category
def frequent_category():
    df = pd.read_csv(file_name)

    print(df['Category'].mode()[0])

# Weekly Spending Analysis
def weekly_spending():
    df = pd.read_csv(file_name)

    weekly = df.groupby('Date')['Amount'].sum()

    print(weekly)

# Expense Percentage
def expense_percentage():
    df = pd.read_csv(file_name)

    income = df[df['Type'] == "Income"]['Amount'].sum()
    expense = df[df['Type'] == "Expense"]['Amount'].sum()

    print((expense / income) * 100)

# AI Savings Recommendation
def ai_recommendation():
    df = pd.read_csv(file_name)

    income = df[df['Type'] == "Income"]['Amount'].sum()
    expense = df[df['Type'] == "Expense"]['Amount'].sum()

    if expense > income:
        print("⚠ Reduce spending")
    else:
        print("✅ Savings are good")

# Financial Profile Classification
def financial_profile():
    df = pd.read_csv(file_name)

    income = df[df['Type'] == "Income"]['Amount'].sum()
    expense = df[df['Type'] == "Expense"]['Amount'].sum()

    if income > expense:
        print("Saver")
    else:
        print("Spender")

# Duplicate Transaction Detection
def duplicate_detection():
    df = pd.read_csv(file_name)

    print(df.duplicated(subset=['ID']))

# Delete Transaction
def delete_transaction():
    df = pd.read_csv(file_name)

    tid = input("Enter Transaction ID to Delete: ")

    df = df[df['ID'] != tid]

    df.to_csv(file_name, index=False)

    print("✅ Transaction Deleted")

# Main Menu
while True:

    print("\n========== FINANCE TRACKER ==========")

    print("""
1. Add Transaction
2. View Transactions
3. Financial Summary
4. Monthly Expense Analysis
5. Highest Spending Category
6. Monthly Savings
7. Average Daily Spending
8. Transaction Frequency
9. Category-wise Spending Trend
10. High Expense Detection
11. Income vs Expense Ratio
12. Most Frequent Spending Category
13. Weekly Spending Analysis
14. Expense Percentage
15. AI Savings Recommendation
16. Financial Profile Classification
17. Duplicate Transaction Detection
18. Delete Transaction
19. Exit
""")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        add_transaction()

    elif choice == '2':
        view_transactions()

    elif choice == '3':
        financial_summary()

    elif choice == '4':
        monthly_expense()

    elif choice == '5':
        highest_spending()

    elif choice == '6':
        monthly_savings()

    elif choice == '7':
        average_spending()

    elif choice == '8':
        transaction_frequency()

    elif choice == '9':
        spending_trend()

    elif choice == '10':
        high_expense()

    elif choice == '11':
        income_expense_ratio()

    elif choice == '12':
        frequent_category()

    elif choice == '13':
        weekly_spending()

    elif choice == '14':
        expense_percentage()

    elif choice == '15':
        ai_recommendation()

    elif choice == '16':
        financial_profile()

    elif choice == '17':
        duplicate_detection()

    elif choice == '18':
        delete_transaction()

    elif choice == '19':
        print("Exiting...")
        break

    else:
        print("Invalid Choice")