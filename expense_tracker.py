import json         
def add_expense():
    name = input("enter name of expense ").strip()
    try:
        amount = float(input("enter amount"))
    except ValueError:
        print("Please enter valid no.")
        return    
    with open("expenses.json" , "r") as f:
        data = json.load(f)
    data.append(
        {
            "name" : name ,
            "amount" : amount
        })    
    with open("expenses.json", "w") as f:
        json.dump(data , f , indent = 4)
    print("expense added successfully")    
def view_expenses():
    try:
        with open ("expenses.json" , "r") as f:
            data = json.load(f)
        if len(data)== 0 :
            print("no expenses found")
            return    
        for expense in data:
            print(expense["name"],"-",expense["amount"])
    except FileNotFoundError:
        print("No Expenses found")
def total_expenses():
    try:
        overall_total = 0
        with open("expenses.json","r") as f:
            data= json.load(f)
            if not data:
                print("no expense found")
                return
            for expense in data: 
                overall_total += expense["amount"]
            print("overall total:",overall_total)
    except FileNotFoundError:
        print("No file found for expenses")        
             

def search_expenses():
    name = input("enter name to search").strip()
    with open("expenses.json" , "r") as f:
        data = json.load(f)
    for expense in data:
        if expense["name"].lower() == name.lower() :
            print(expense["name"],"-", expense["amount"])    
            return
    print("no record found")    

def update_expenses():
    name = input("enter name to update").strip()
    with open("expenses.json" , "r") as f:
        data = json.load(f)
    for expense in data:
        if expense["name"].lower() == name.lower() :
            new_name = input("enter updated name")
            new_amount = float(input("enter updated amount"))
            expense["name"] = new_name
            expense["amount"] = new_amount 
        with open("expenses.json" , "w") as f:
            json.dump(data , f , indent = 4)                   

    
        print("updated successfully")
        return
    print("no record found")

def delete_expenses():
    name = input("enter name of expense to delete")
    with open("expenses.json" , "r") as f:
        data = json.load(f)
    for expense in data:
        if expense["name"] == name :
            data.remove(expense)
            with open("expenses.json" , "w") as f:
                json.dump(data , f ,indent = 4)
            print("Expense deleted successfully")    
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

