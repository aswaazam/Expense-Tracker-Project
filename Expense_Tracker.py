expenses = []

def add_expense():
    user_expense_name = input("Enter expense name: ")
    user_expense_amount = int(input("Enter expense amount: "))
    user_expenses = {"name":user_expense_name, "amount":user_expense_amount}
    expenses.append(user_expenses)
    print(expenses)

def view_expenses():
    if expenses == []:
        print("No expenses found yet.")
    else: 
        print(expenses)

def calculate_expenses():
    total_expense = 0
    if expenses == []:
        print("Your total expense is 0rs.")
    else:
        for i in expenses:
            total_expense += i["amount"]
        print("Total expenses are:", total_expense, "rs")

while True:
    try:
        user_choice =  int(input("Enter your choice: \n" \
        "1. Add Expense\n" \
        "2. View Expenses\n" \
        "3. Calculate Total\n" \
        "4. Exit\n"))

    except ValueError:
        print("Enter a valid number.")
        continue

    if user_choice == 1:
        add_expense()
    elif user_choice == 2:
        view_expenses()
    elif user_choice == 3:
        calculate_expenses()
    elif user_choice == 4:
        print("Thankyou!")
        exit()
    else:
        print("Please enter a valid value")
