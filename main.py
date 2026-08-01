import csv
import os
from datetime import date

print("================================")
print("     STUDENT EXPENSE TRACKER")
print("================================")

# File paths
project_folder = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(project_folder, "data")
file_path = os.path.join(data_folder, "expenses.csv")
budget_file = os.path.join(project_folder, "budget.txt")

# Make sure data folder exists
os.makedirs(data_folder, exist_ok=True)

# Store expenses
expenses = []

# Available categories
categories = {
    "1": "Food",
    "2": "Travel",
    "3": "Education",
    "4": "Shopping",
    "5": "Bills",
    "6": "Other"
}


# Load previously saved expenses
if os.path.exists(file_path):

    with open(file_path, "r", newline="") as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            if len(row) == 4:

                expense_date = row[0]
                expense_name = row[1]
                amount = float(row[2])
                category = row[3]

                expenses.append([
                    expense_date,
                    expense_name,
                    amount,
                    category
                ])

            elif len(row) == 3:

                expense_name = row[0]
                amount = float(row[1])
                category = row[2]

                expenses.append([
                    "Unknown",
                    expense_name,
                    amount,
                    category
                ])


# Load budget
budget = 0

if os.path.exists(budget_file):

    with open(budget_file, "r") as file:

        budget_text = file.read().strip()

        if budget_text:

            try:
                budget = float(budget_text)

            except ValueError:
                budget = 0


# Save expenses
def save_expenses():

    with open(file_path, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Expense Name",
            "Amount",
            "Category"
        ])

        for expense in expenses:

            writer.writerow(expense)


# Add expense
def add_expense():

    print("\n----------- ADD EXPENSE -----------")

    expense_date = str(date.today())

    # Expense name
    while True:

        expense_name = input(
            "\nEnter expense name: "
        ).strip()

        if expense_name:

            break

        print(
            "Expense name cannot be empty!"
        )


    # Amount
    while True:

        amount_input = input(
            "Enter expense amount: "
        ).strip()

        try:

            amount = float(amount_input)

            if amount <= 0:

                print(
                    "Amount must be greater than 0."
                )

            else:

                break

        except ValueError:

            print(
                "Invalid amount! "
                "Please enter a number."
            )


    # Category
    print("\nSelect Category:")

    for number, category in categories.items():

        print(
            f"{number}. {category}"
        )


    while True:

        category_choice = input(
            "\nEnter category number (1-6): "
        ).strip()

        if category_choice in categories:

            category = categories[
                category_choice
            ]

            break

        print(
            "Invalid category! "
            "Please enter a number from 1 to 6."
        )


    expenses.append([
        expense_date,
        expense_name,
        amount,
        category
    ])


    save_expenses()


    print(
        "\nExpense added successfully! ✅"
    )

    print(
        f"Date: {expense_date}"
    )


# View expenses
def view_expenses():

    print(
        "\n----------- ALL EXPENSES -----------"
    )


    if not expenses:

        print(
            "No expenses found."
        )

        return


    for number, expense in enumerate(
        expenses,
        start=1
    ):

        print(
            f"{number}. "
            f"Date: {expense[0]} | "
            f"Name: {expense[1]} | "
            f"Amount: ₹{expense[2]:.2f} | "
            f"Category: {expense[3]}"
        )


# View total
def view_total():

    print(
        "\n----------- TOTAL EXPENSE -----------"
    )


    total = sum(
        expense[2]
        for expense in expenses
    )


    print(
        f"Total Expenses: ₹{total:.2f}"
    )


# Category analysis
def category_analysis():

    print(
        "\n----------- CATEGORY ANALYSIS -----------"
    )


    if not expenses:

        print(
            "No expenses found."
        )

        return


    category_totals = {}


    for expense in expenses:

        category = expense[3]
        amount = expense[2]


        if category in category_totals:

            category_totals[category] += amount

        else:

            category_totals[category] = amount


    for category in categories.values():

        amount = category_totals.get(
            category,
            0
        )


        print(
            f"{category:<12}: ₹{amount:.2f}"
        )


    total = sum(
        expense[2]
        for expense in expenses
    )


    print(
        "-----------------------------------------"
    )

    print(
        f"{'Total':<12}: ₹{total:.2f}"
    )


# Search expenses
def search_expenses():

    print(
        "\n----------- SEARCH EXPENSES -----------"
    )


    if not expenses:

        print(
            "No expenses found."
        )

        return


    search_term = input(
        "Enter expense name or category to search: "
    ).strip().lower()


    if not search_term:

        print(
            "Search term cannot be empty."
        )

        return


    matching_expenses = []


    for expense in expenses:

        expense_name = expense[1].lower()
        category = expense[3].lower()


        if (
            search_term in expense_name
            or search_term in category
        ):

            matching_expenses.append(
                expense
            )


    if not matching_expenses:

        print(
            "\nNo matching expenses found."
        )

        return


    print(
        "\n----------- SEARCH RESULTS -----------"
    )


    search_total = 0


    for number, expense in enumerate(
        matching_expenses,
        start=1
    ):

        print(
            f"{number}. "
            f"Date: {expense[0]} | "
            f"Name: {expense[1]} | "
            f"Amount: ₹{expense[2]:.2f} | "
            f"Category: {expense[3]}"
        )

        search_total += expense[2]


    print(
        "-----------------------------------------"
    )

    print(
        f"Matching Expenses: "
        f"{len(matching_expenses)}"
    )

    print(
        f"Matching Total: "
        f"₹{search_total:.2f}"
    )


# Delete expense
def delete_expense():

    print(
        "\n----------- DELETE EXPENSE -----------"
    )


    if not expenses:

        print(
            "No expenses found."
        )

        return


    for number, expense in enumerate(
        expenses,
        start=1
    ):

        print(
            f"{number}. "
            f"Date: {expense[0]} | "
            f"Name: {expense[1]} | "
            f"Amount: ₹{expense[2]:.2f} | "
            f"Category: {expense[3]}"
        )


    while True:

        choice = input(
            "\nEnter expense number to delete: "
        ).strip()


        try:

            expense_number = int(choice)


            if (
                expense_number < 1
                or expense_number > len(expenses)
            ):

                print(
                    "Invalid expense number!"
                )

            else:

                break


        except ValueError:

            print(
                "Please enter a valid number."
            )


    deleted_expense = expenses.pop(
        expense_number - 1
    )


    save_expenses()


    print(
        "\nExpense deleted successfully! 🗑️"
    )


    print(
        f"Deleted: {deleted_expense[1]} "
        f"| ₹{deleted_expense[2]:.2f} "
        f"| {deleted_expense[3]}"
    )


# Set budget
def set_budget():

    global budget

    print(
        "\n----------- SET BUDGET -----------"
    )


    while True:

        budget_input = input(
            "Enter your budget amount: "
        ).strip()


        try:

            new_budget = float(
                budget_input
            )


            if new_budget <= 0:

                print(
                    "Budget must be greater than 0."
                )

            else:

                break


        except ValueError:

            print(
                "Invalid amount! "
                "Please enter a number."
            )


    budget = new_budget


    with open(
        budget_file,
        "w"
    ) as file:

        file.write(
            str(budget)
        )


    print(
        f"\nBudget set successfully! "
        f"₹{budget:.2f}"
    )


# View budget
def view_budget():

    print(
        "\n----------- BUDGET STATUS -----------"
    )


    if budget <= 0:

        print(
            "No budget has been set."
        )

        return


    total = sum(
        expense[2]
        for expense in expenses
    )


    remaining = budget - total


    print(
        f"Budget:    ₹{budget:.2f}"
    )

    print(
        f"Spent:     ₹{total:.2f}"
    )

    print(
        f"Remaining: ₹{remaining:.2f}"
    )


    percentage = (
        total / budget
    ) * 100


    print(
        f"Used:      {percentage:.1f}%"
    )


    if percentage >= 100:

        print(
            "\n⚠️ WARNING: "
            "You have exceeded your budget!"
        )

    elif percentage >= 80:

        print(
            "\n⚠️ WARNING: "
            "You have used more than 80% "
            "of your budget."
        )

    else:

        print(
            "\n✅ You are within your budget."
        )


# Main menu
while True:

    print(
        "\n================================"
    )

    print(
        "           MAIN MENU"
    )

    print(
        "================================"
    )

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Category Analysis")
    print("5. Search Expenses")
    print("6. Delete Expense")
    print("7. Set Budget")
    print("8. View Budget")
    print("9. Exit")


    choice = input(
        "\nEnter your choice (1-9): "
    ).strip()


    if choice == "1":

        add_expense()


    elif choice == "2":

        view_expenses()


    elif choice == "3":

        view_total()


    elif choice == "4":

        category_analysis()


    elif choice == "5":

        search_expenses()


    elif choice == "6":

        delete_expense()


    elif choice == "7":

        set_budget()


    elif choice == "8":

        view_budget()


    elif choice == "9":

        print(
            "\nThank you for using "
            "Student Expense Tracker!"
        )

        print(
            "Goodbye! 👋"
        )

        break


    else:

        print(
            "\nInvalid choice! "
            "Please enter a number from 1 to 9."
        )