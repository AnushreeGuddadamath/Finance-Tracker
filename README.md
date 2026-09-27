# Finance Tracker

## Project Description

Finance Tracker is a Python-based personal finance management system that helps users record income and expenses, analyze spending patterns, track savings, detect duplicate transactions, and generate financial insights. The application uses Pandas for data analysis and stores data in CSV files through a menu-driven interface.

---

## Introduction

Finance Tracker is designed to help individuals manage their personal finances effectively. The system allows users to record financial transactions, monitor income and expenses, analyze spending behavior, and generate useful financial insights.

### Key Features

- Record Income and Expense Transactions
- Track Monthly Spending
- Analyze Savings
- Identify Highest Spending Categories
- Monitor Spending Trends
- Detect Duplicate Records
- Generate AI-Based Recommendations
- Financial Profile Classification
- CSV-Based Data Storage

---

## Objectives

- Develop a menu-driven finance management application using Python.
- Store and manage transaction data using CSV files.
- Analyze financial records using Pandas.
- Generate financial insights and recommendations.
- Improve financial awareness through reports and spending analysis.

---

## Technologies Used

- Python
- Pandas
- CSV File Handling
- NumPy (for analysis support)

---

## Business Research Questions

1. How much money is being spent every month, and is the spending under control?
2. Which expense category consumes the largest portion of income?
3. Is the user saving enough money after monthly expenses?
4. What is the user's average daily spending behavior?
5. How active is the user financially based on transaction frequency?
6. Which spending categories show the highest financial trends over time?
7. Are there any unusually high expenses affecting financial stability?
8. Is the user maintaining a healthy balance between income and expenses?
9. Which category reflects the user's most frequent spending habit?
10. What are the most recent financial activities performed by the user?
11. During which weeks does the user tend to overspend the most?
12. What percentage of income is consumed by expenses?
13. Can the system intelligently recommend ways to improve savings?
14. Is the user financially a "Saver" or a "Spender"?
15. Are duplicate financial records affecting transaction accuracy?

---

## Functionalities

### 1. Add Transaction
Allows users to add income or expense records with:
- Transaction ID
- Type
- Category
- Amount
- Date

### 2. View Transactions
Displays all stored transactions.

### 3. Financial Summary
Shows:
- Total Income
- Total Expense
- Remaining Balance

### 4. Monthly Expense Analysis
Calculates total monthly expenses.

### 5. Highest Spending Category
Identifies the category where the user spends the most money.

### 6. Monthly Savings
Calculates:

Savings = Total Income - Total Expense

### 7. Average Spending
Calculates average transaction amount.

### 8. Transaction Frequency
Counts total transactions performed.

### 9. Spending Trend Analysis
Displays category-wise spending trends.

### 10. High Expense Detection
Identifies transactions above a defined threshold.

### 11. Income vs Expense Ratio
Measures financial stability using:

Ratio = Income / Expense

### 12. Frequent Spending Category
Finds the most frequently used spending category.

### 13. Weekly Spending Analysis
Analyzes spending patterns by week.

### 14. Expense Percentage
Calculates:

Expense Percentage = (Expense / Income) × 100

### 15. AI Savings Recommendation
Provides recommendations based on spending behavior.

Example:
- Reduce spending if expenses exceed income.
- Encourage savings when financial performance is healthy.

### 16. Financial Profile Classification

Categories:
- Saver
- Spender

### 17. Duplicate Transaction Detection
Detects duplicate transaction IDs.

### 18. Delete Transaction
Removes transactions from the dataset.

---

## Project Workflow

1. User enters transaction details.
2. Data is stored in CSV format.
3. Pandas reads transaction data.
4. Analysis functions process records.
5. Reports and insights are generated.
6. User reviews financial performance.

---

## Sample Dataset Structure

| ID | Type | Category | Amount | Date |
|----|------|----------|--------|------|
| 1 | Income | Salary | 50000 | 01-05-2026 |
| 2 | Expense | Food | 2500 | 01-05-2026 |
| 3 | Expense | Shopping | 3500 | 02-05-2026 |

---

## Key Insights Generated

### Monthly Spending Analysis
Helps identify whether expenses exceed income.

### Highest Spending Category
Shows where most money is spent.

### Savings Analysis
Measures financial health and saving potential.

### Spending Trends
Highlights categories consuming most resources.

### Expense Monitoring
Detects unusually high expenses.

### Financial Stability
Measures balance between income and expenditure.

### Spending Habits
Identifies the most frequent expense categories.

### Duplicate Detection
Ensures data accuracy and reliability.

---

## Advantages

- Easy to Use
- Menu-Driven Interface
- Lightweight Application
- No Database Required
- Accurate Financial Tracking
- Useful Financial Insights
- Supports Budget Planning

---

## Future Enhancements

- MySQL Database Integration
- User Authentication System
- Dashboard Visualization
- PDF Report Generation
- Excel Export Functionality
- Machine Learning-Based Expense Prediction
- Web Application using Flask/Django

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Finance-Tracker.git
```

### Install Dependencies

```bash
pip install pandas
```

### Run Application

```bash
python "Finance Tracker (Main).py"
```

---

## Menu Options

```text
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
```

---

## Conclusion

Finance Tracker is a comprehensive Python-based personal finance management application that enables users to track income, manage expenses, monitor savings, analyze spending behavior, and make informed financial decisions. The project demonstrates practical implementation of Python, Pandas, file handling, and data analytics concepts in a real-world finance management scenario.

## Author

Developed as a Python Finance Tracker Project using Python and Pandas for personal finance analysis and management.
