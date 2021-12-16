while True:
    print("WELCOME TO BANK OF BARODA")
    print("Choose any option")
    print("1. Withdrawal Money")
    print("2.Update pin")
    print("3.Exit ")
    choice=int(input("Enter your option:  "))
    total=100000
    if choice==1:
        a=int(input("Who much you want to withdraw : "))
        c=total-a
        print("Please wait............")
        print("collect your amount")
        print("Do you Want to see your available balance \n 1.Yes \n 2.No")
        choose=int(input("your option =1/2 : "))
        if choose==1:
            print("Your Available balance is : ",c
                  )
        else:
            print("ok")
    elif choice==2:
        password=int(input("Enter your password"))
        if password==8287:
            password2=int(input("Enter your new Pin"))
            password2=int(input("Re-enter your Pin"))
            print("Password Updated")

    elif choice==3:
        print("Thank you for visiting ")
        break
            
    
