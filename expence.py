FILE_NAME = "expenses.txt"   

def load_expenses():
    """Read old expenses from the file and return them as a list."""
    expenses = []
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(",")         
                expenses.append([parts[0], parts[1], float(parts[2])])
        file.close()
    except FileNotFoundError:
        pass                                  
    return expenses

def save_expenses(expenses):
    """Write the full list of expenses to the file."""
    file = open(FILE_NAME, "w")
    for item in expenses:
        file.write(item[0] + "," + item[1] + "," + str(item[2]) + "\n")
    file.close()


def add_expense(expenses):
    """Ask the user for details and add a new expense."""
    name = input("Enter expense name (e.g. Lunch): ").replace(",", " ")
    category = input("Enter category (e.g. Food, Travel, Books): ").replace(",", " ")
    try:
        amount = float(input("Enter amount in Rs: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    expenses.append([name, category, amount])
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    """Show all expenses in a simple table."""
    if len(expenses) == 0:
        print("No expenses found.")
        return
    print("\nNo.  Name               Category         Amount")
    print("-" * 50)
    number = 1
    for item in expenses:
        print(str(number).ljust(5) + item[0].ljust(19) + item[1].ljust(17) + str(item[2]))
        number = number + 1


def show_total(expenses):
    """Show total spending and the biggest expense."""
    if len(expenses) == 0:
        print("No expenses found.")
        return
    total = 0
    biggest = expenses[0]
    for item in expenses:
        total = total + item[2]
        if item[2] > biggest[2]:
            biggest = item
    print("\nTotal spent      : Rs", total)
    print("Biggest expense  :", biggest[0], "- Rs", biggest[2])


def delete_expense(expenses):
    """Delete an expense by its number."""
    view_expenses(expenses)
    if len(expenses) == 0:
        return
    try:
        number = int(input("Enter the number to delete: "))
        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            save_expenses(expenses)
            print("Deleted:", removed[0])
        else:
            print("Number not in list.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main menu of the program."""
    expenses = load_expenses()
    print("===== SIMPLE EXPENSE TRACKER =====")
    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Thank you! Goodbye.")
            break
        else:
            print("Wrong choice! Please enter 1 to 5.")


main()