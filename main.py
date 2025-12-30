                                        #   Expense Tracker Project


expense = []
import time
anything_numner= int(input("Enter enything number--->"))
for _ in range(anything_numner,0,-1):
    print("🧡"*_+ "----->🍀WELCOME TO EXPENSE TRACKER🍀")
    time.sleep(0.2)

while True:
   
    print("1.<==============🍀MENU🍀==============>")
    print("2.<=ADD EXPENSE=>")
    print("3.<=VIEW ALL EXPENSE=>")
    print("4.<=VIEW TOTAL EXPENSE=>")
    print("5.<=EXIT=>")

    choice= int(input("Eenter your choice---->"))
                                                                  # Add expense
    if choice == 1:
        date= input("Enter the spending date----->")
        category= input ("Tyape spending\nfood,treval,mekeup,books--->")
        amount = float(input("Enter amount--->"))
        description= input("Enter the other detail\n--->")
        amount= float(input ("Enter the amount\nAMOUNT--->"))

        expense_dic= {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount,
              }
        expense.append(expense_dic)
        print("\nDOEN Expense is added succesfully")


    elif choice == 2:                                            #view all expense
        if len(expense)== 0:
            print ("not expense added plese add your expense")
        else:
            print ("total spending---->")  
            count= 1
            for eachspending in expense:
                print(f"eachspending number{count}--->,{eachspending['date']},{eachspending['category']},{eachspending['description']},{eachspending['amount']}")
                count += 1
    
    elif choice == 3:                                            #view total spending
        total= 0
        for eachspending in expense:
            total += eachspending['amount']
            print("total all spending---->",total)
    
    elif choice == 4:                                             # Exit
        print ("thanyou for using  my system")
        break
    else:
        print("invalid choice")                    


