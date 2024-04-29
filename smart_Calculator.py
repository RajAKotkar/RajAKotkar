
print("\n-------------------SMART CALCULATOR-------------------")

print("\nENTER THE INPUTS NUMBERS ON WHICH YOU WANTS TO PERFORM AN OPERAATIONS")

a=int(input("\nEnter the first number: "))
b=int(input("Enter the second number: "))


print("\n=======MENU=======")
print("Choose 1 for addition")
print("Choose 2 for substraction")
print("Choose 3 for multiplication")
print("Choose 4 for division")
print("choose 5 for EXIT")



while True:
    choice=int(input("\nEnter the number from 1-5 to select an option: "))
    if choice == 1:
        print("\nYou choose option 1(addition) and your ans is: ",(a+b))
    elif choice == 2:
        print("\nYou choose option 2(substraction) and your ans is: ",(a-b))
    elif choice == 3:
        print("\nYou choose option 3(multiplication) and your ans is: ",(a*b))
    elif choice == 4:
        print("\nYou choose option 4(division) and your ans is: ",(a/b))
    elif choice == 5:
        print("YOU ARE EXITED")
        break
    else :
        print("\nOPTION INVALID")    
    