expenses= []
def add_expense():
    name = input("enter name of expense ")
    amount = float(input("enter amount"))

    expense = {
        "name" : name ,
        "amount" : amount
    }   
    expenses.append(expense)
    print("expense added successfully")

def view_expenses():
    if len(expenses) == 0 :
        print("no record found")
    else:
        for expense in expenses:
            print("^^^^Expense list^^^^^^")
            print("Name of expense:", expense["name"]) 
            print("amount of expense", expense["amount"])


def total_expenses():
    total=0
    for expense in expenses:
        total = total + expense["amount"]
    print("total expense: ",total) 

def search_expenses():
    name = input("enter name to search")
    found = False
    for expense in expenses:
        if expense["name"] == name:
            print("name:", expense["name"])
            print("amount:", expense["amount"])

def update_expenses():
    name = input("enter name to update")
    for expense in expenses:
        if expense["name"] == name:
            new_name = input("enter updated name")
            new_amount = float(input("enter updated amount"))
            
            expense["name"] = new_name
            expense["amount"] = new_amount
            print("updated successfully")
            return
    print("no record found")

def delete_expenses():
    name = input("enter name of expense to delete")
    for expense in expenses:
        if expense["name"]== name:
            expenses.remove(expense)
            print("expense remmoved successfully")
            return
    print("no record found")


while True:
    print("\n^^^^^^^^EXPENSE TRACKER^^^^^^")
    print("1. Add expense")
    print("2. view Expenses")
    print("3. Total Expenses ")
    print("4. Search an expense ")
    print("5. Update an expense")
    print("6. delete an expense")
    print("7. exit ")

    choice = input("enter your choice ")




    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        search_expenses()
    elif choice == "5":
        update_expenses()
    elif choice == "6":
        delete_expenses()
    elif choice == "7":
        print("exiting")
        break
    else:
        print("invalid output")                              

