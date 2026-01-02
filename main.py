                                        #  EXPENSE TRACKER (No Functions)
# ----------------------------------- 
# EXPENSE TRACKER (No Functions) 
# -----------------------------------

expense = []                                                                         # list of expense dictionaries 
import time
anything_numner= int(input("Enter (1 to 5) number--->"))
for _ in range(anything_numner,0,-1):
    print("🧡"*_+ "----->🍀WELCOME TO EXPENSE TRACKER🍀")
    time.sleep(0.2)

  
 
print("\🍀🍀🍀nWelcome to Expense Tracker🍀🍀🍀 ".upper()) 
 
while True: 
    print("\n======= MENU =======") 
     
     
    print("1⃣ Add Expense") 
    print("2⃣ View All Expenses") 
    print("3⃣ View Total Spending") 
    print("4⃣ View Spending by Category") 
    print("5⃣ Exit") 
    print("=====================") 
 
    choice = input("Enter your choice (1-5): ")
 
                                                                                        # 1⃣ Add Expense 
    if choice == "1": 
        date = input("Enter date DD-MM-YYYY: ")
        category = input("Enter category (Food, Travel, Shopping,etc): ")   
        description = input("Enter short description: ") 
        amount = float(input("Enter amount (₹): ")) 
 
        expenses = {                                                                   # Dicdictionaries expenses                                     
            "date": date, 
            "category": category, 
            "description": description, 
            "amount": amount, 
        } 
        expense.append(expenses) 
        print("\n✅Expense added successfully!") 
 
                                                                                       # 2⃣ View All Expenses 
    elif choice == "2": 
        if len(expense) == 0: 
            print("\n⚠No expenses recorded yet.") 
        else: 
            print("\n--- All Expenses ---") 
            i = 1 
            for e in expense: 
                print(f"{i}.{e['date']} | {e['category']} | {e['description']} | {e['amount']}") 
                i += 1 
            print("---------------------") 
 
                                                                                       # 3⃣ View Total Spending 
    elif choice == "3": 
        total = 0 
        for e in expense: 
            total += e['amount'] 
        print(f"\n💰Total Spending = ₹{total}")
 
                                                                                        # 4⃣ Spending by Category 
    elif choice == "4": 
        if len(expense) == 0: 
            print("\n⚠ No expenses recorded yet.") 
        else: 
            summary = {} 
            for e in expense: 
                cat = e["category"] 
                if cat in summary: 
                    summary[cat] += e['amount'] 
                else: 
                    summary[cat] = e['amount'] 
 
            print("\n📊Spending by Category:") 
            for cat, amt in summary.items():
                 print(f"{cat}: ₹{amt}") 
 
                                                                                         # 5⃣ Exit 
    elif choice == "5": 
        print("\n👋Thanks for using Expense Tracker! Bye!") 
        break 
 
    else: 
        print("\n❌Invalid choice. Please try again.")
                 


