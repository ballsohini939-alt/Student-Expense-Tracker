# 💰 Student Expense Tracker

### A Python CLI Application for Smarter Expense Management

A command-line application that helps users record daily expenses, analyze spending patterns, organize transactions by category, and monitor their budgets.

Built with Python, this project demonstrates practical programming concepts through a functional expense-management application with local data persistence.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Interface-CLI-181717?style=for-the-badge&logo=windows-terminal&logoColor=white" alt="Command Line Interface">
  <img src="https://img.shields.io/badge/Storage-CSV-217346?style=for-the-badge&logo=files&logoColor=white" alt="CSV Storage">
</p>

---

## 📌 Overview

Managing everyday expenses can be difficult without a clear record of spending.

**Student Expense Tracker** provides a simple way to record expenses, review spending by category, search transactions, and compare total spending against a personal budget.

Expense records are stored locally using CSV file handling, while budget information is saved separately.

## ✨ Features

| Feature               | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| ➕ Expense Management  | Add and record daily expenses                                    |
| 📅 Automatic Dates    | Record the current date when adding an expense                   |
| 📋 Expense History    | View saved expense records                                       |
| 💵 Total Calculation  | Calculate total recorded expenses                                |
| 📊 Category Analysis  | Review spending across expense categories                        |
| 🔎 Search             | Find expenses by name or category                                |
| 🗑️ Delete            | Remove an expense by selecting its record                        |
| 🎯 Budget Management  | Set and view a personal budget                                   |
| 📈 Budget Monitoring  | Calculate spending, remaining budget, and percentage used        |
| ⚠️ Budget Warnings    | Receive warnings when spending reaches 80% or exceeds the budget |
| 💾 Persistent Storage | Save expense and budget data locally                             |
| 🛡️ Input Validation  | Handle invalid amounts, menu choices, and other user input       |

## 🛠️ Technology Stack

* **Python** — Application logic and program flow
* **CSV** — Expense record storage
* **File Handling** — Reading and writing local data
* **Lists and Dictionaries** — Managing expenses and categories
* **Functions** — Organizing application operations
* **Exception Handling** — Handling invalid numeric input
* **`datetime`** — Recording expense dates

## 📁 Project Structure

```text
Student-Expense-Tracker/
│
├── data/
│   ├── .gitkeep
│   └── expenses.csv       # Created when expense data is saved
│
├── main.py                # Application entry point
├── budget.txt             # Created when a budget is saved
├── .gitignore
└── README.md
```

**Note:** `expenses.csv` and `budget.txt` are generated during application use. Personal expense records and budget information should remain local and should not be committed to GitHub.

## 🚀 Getting Started

### Prerequisites

* Python 3 installed
* A terminal or command prompt

Verify your Python installation:

```bash
python --version
```

On systems that use `python3`, run:

```bash
python3 --version
```

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ballsohini939-alt/Student-Expense-Tracker.git
```

**2. Navigate to the project directory**

```bash
cd Student-Expense-Tracker
```

**3. Run the application**

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

No third-party Python packages are required for the application's documented core functionality.

## 🖥️ Application Menu

The application provides a simple menu-driven interface:

```text
================================
 MAIN MENU
================================
1. Add Expense
2. View Expenses
3. View Total
4. Category Analysis
5. Search Expenses
6. Delete Expense
7. Set Budget
8. View Budget
9. Exit
```

Select an option to perform the corresponding operation.

## 🧠 Concepts Demonstrated

This project applies several foundational Python concepts:

* Variables and data types
* Conditional statements and loops
* Functions and modular programming
* Lists and dictionaries
* CSV processing
* File handling and persistent storage
* Exception handling
* Date handling
* Input validation
* Basic financial calculations

## 🔮 Future Enhancements

Potential improvements for future versions include:

* Monthly and weekly expense summaries
* Editing existing expenses
* Graphical user interface
* Data visualization and spending charts
* Database integration
* Exportable expense reports

These are planned enhancements, not features currently claimed as implemented.

## 👩‍💻 Author

**Sohini Ball**
B.Tech Computer Science and Engineering Student

[GitHub Profile](https://github.com/ballsohini939-alt) · [LinkedIn Profile](https://www.linkedin.com/in/sohini-ball-698012381/)

---

⭐ If you find this project useful, feel free to explore the code and suggest improvements.

