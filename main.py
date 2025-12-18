  GNU nano 8.6                                                        main.py


                         #✅✅✅✅mini expense treacker project✅✅✅✅

#creat a console  based expense tracker program in python that aloww the user allow user to daily
#expense and viwe summaries like total spending . use only consept learn till chepter -6
#(conditionals, dictionaries and basic, input output loops)

# project details / deacription
# your are required to built a simple personal fineance managment tool. the program should aloww
# user to
# 1- add an expense with details categary description and amount
# 2- view all receorded expanse in clean format
# 3- calculate total spending so for
# 4- exit thevprogram gracefully when the user choice
print ("=============================================================================")
print ("==🔷🔷️🔷️   💓    💓   💛💛💛💛   🔷️🔷️🔷️🔷️   🔶️      🔶️  🌳🌳🌳🌳  🔷️🔷️🔷️🔷️ ==")
print ("==🔷️        💓 💓     💛    💛   🔷️         🔶️ 🔶️   🔶️  🌳        🔷️       ==")
print ("==🔷️🔷️🔷️      💓       💛💛💛💛   🔷️🔷️🔷️🔷️   🔶️  🔶️  🔶️  🌳🌳🌳🌳  🔷️🔷️🔷️🔷️==")
print ("==🔷️         💓 💓     💛         🔷️         🔶️   🔶️ 🔶️        🌳  🔷️      ==")
print ("==🔷️🔷️🔷️   💓    💓    💛         🔷️🔷️🔷️🔷️   🔶️    🔶️🔶️  🌳🌳🌳🌳  🔷️🔷️🔷️🔷️==")
print ("==================////////////============///////////=======================")

import time
expenselist = []       #list of eexpenes
i = 1
while i<=3:
        print ("🔱🔱🌹🌼🙏WELCOME🙏🌼🌹🔱🔱TO EXPENSE TRACKE\n🌹🌹🌹🌹 बचत का हे मोल मीलक्र नीभाए ये रोल🌹🌹🌹🌹🌹")
        i+=1
        time.sleep(0.1)

while True:
    print ("💠💠🏵🏵🏵💠💠MENU💠💠🏵🏵🏵💠💠")
    print ("1. Add expense")
    print ("2. View all expenses")
    print ("3. view total amount")
    print ("4. Quit")

    choice = int(input("Enter your choice: "))       # Add  user input for choice

    if choice == 1:
        date = input("Enter the spending date: ")
        category = input("Type of category spending food, travel, cloth, domestic, books, gadgets: ")
        description = input("Enter other detail: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }
        expenselist.append(expense)  # Append the dictionary to the list
        print("DON✅✅ BRO,🌹expense is added✅ successfully🌹")

    elif choice == 2:
        if len(expenselist) == 0:
            print ("No❌ expenses❌ added")
        else:
            print ("===🌹 Your all expenses🌹 ===")
            count = 1
            for eachspending in expenselist:
                print (f"Spending number {count} -> {eachspending['date']}, {eachspending['category']}, {eachspending['amount']}, {eachspending>
                count += 1

    elif choice == 3:   #view total spending
        total = 0
        for eachspending in expenselist:
            total += eachspending['amount']
        print ("Total spending =", total)

    elif choice == 4:
        print ("🌹🌹🌹Thank you for🌼🌼🌼 using my system🌹🌹🌹")
        break                        # Correctly indented break inside the while loop

    else:
        print ("Invalid choice, try")
