# Cyliender Booking in Python ,
# Real life project.
# Based Point:-
# Introduction : Welcome To Hp Anytime....
# Select Your choices : a) Cylinder booking , b)Regenerate password, c)Create new account, d)Issue , e)Help;

"""A single Customer details, It's a basic cylinder booking 
   So we can login only predifind data."""

"""**************************************"""
"""Customer ID: ayanabha5263
   Password: pass
   Phone Number: 9007328820
   Cylinder Rate: 1100Rs
   Cards: a) Rupa - 7845
          b) Mastercard - 8745
          c) Visa -  4587
          d) Credit Card - 5784 
   Membership ID: memberayan789"""
"""**************************************"""
"""This project is still under devolopment.
   It's update version release comming soon!"""


def cybooking(CID, Password):
    print("Booking Cylinder```")
    while True:
        if CID == "ayanabha5263" and Password == "pass":
            print("OK!")
        else:
            print("Incorrect Passord!")
            break
        phoneNumber = int(input("Now enter your Valid phone number: "))
        if phoneNumber == 9007328820:
            print("Pass!")
        else:
            print("Incorrect Phone Number!")
            break
        print("Current Cylinder rate in market ,`1100Rs`")
        payMoney = int(input("Rs , "))
        if payMoney == 1100:
            print("Check!")
        else:
            print("Please Pay Full Money!")
            break
        card = str(
            input(
                "---Select a card---  \n a~Rupay \n b~MasterCard \n c~Visa \n d~CreditCard \n > "
            )
        )
        if card == "a":
            pin = int(input("Enter Your PIN = "))
            if pin == 7845:
                print("Booking Done!")
                print("Thanks for calling us.")
            else:
                print("Sorry! [Somthing Wrong]")
                break
        elif card == "b":
            pin = int(input("Enter Your PIN = "))
            if pin == 8745:
                print("Booking Done!")
                print("Thanks for calling us.")
            else:
                print("Sorry! [Somthing Wrong]")
                break
        elif card == "c":
            pin = int(input("Enter Your PIN = "))
            if pin == 4587:
                print("Booking Done!")
                print("Thanks for calling us.")
            else:
                print("Sorry! [Somthing Wrong]")
                break
        elif card == "d":
            pin = int(input("Enter Your PIN = "))
            if pin == 5784:
                print("Booking Done!")
                print("Thanks for calling us.")
            else:
                print("Sorry! [Somthing Wrong]")
                break
        else:
            print("ERROR! Please Try Again!")
            break


def repass():
    while True:
        choice = str(
            input(
                "Anypassword issue ,\n 1~Forgot password \n 2~Regenerate password \n 3~Exit \n Please Enter your choice :: "
            )
        )
        if choice == "1":
            print("You forgot your password ....... ")
            passFound = int(input("Enter your valid phone number: "))
            if passFound == 9007328820:
                print("We got your password....")
                print(" `pass` ")
            else:
                print("Error! Please check your number.")
                break
        elif choice == "2":
            print("Regenerate password .......")
            passGenerator = str(input("Enter your previous password : "))
            if passGenerator == "pass":
                print(
                    " `Your new password should be the combination of Charecters, Numbers, Spacial Charecters` "
                )
                newPass = str(input("Enter your new password:  "))
                print(f"Your new password is, {newPass} ")
                print("Save....")
            else:
                print("Incorrect password!")
                break
        elif choice == "3":
            print("`EXIT`")
            break
        else:
            print("ERROR!")
            break


def createAcc():
    while True:
        choice = str(
            input(
                "Account info , \n 1~Create New Account or Recreate your CID \n 2~New Membership \n 3~Exit \n Please Enter your choice: "
            )
        )
        if choice == "1":
            print("Create New Account or Recreate your CID ``` ")
            zzz = str(input("You have already an account , `yes` or `no` :"))
            if zzz == "yes":
                previous = str(input("Enter your previous CID: "))
                if previous == "ayanabha5263":
                    change = str(input("You Change your CID `yes` or `no`: "))
                    if change == "yes":
                        print(
                            " `Your Customer ID should be combination of Charecters, Numbers, Spacial Charecters` "
                        )
                        newCID = str(input("Please Enter your new CID: "))
                        print(f"Your new Customer ID is ,{newCID} ")
                        print("Save")
                    elif change == "no":
                        print("EXIT")
                        break
                    else:
                        print("Please! choice a predefind option. ")
                        break
                else:
                    print("Incorrect CID! Please try again.")
                    break
            elif zzz == "no":
                print(
                    " `Your Customer ID should be combination of Charecters, Numbers, Spacial Charecters` "
                )
                createNew = str("Enter Your Customer ID: ")
                print(f"Your Customer ID is,{createNew} don't forget it !")
                print("Save.....")
            else:
                print("Please! choice a predefind option.")
                break
        elif choice == "2":
            print("New Membership ```")
            uuu = str(input("You have already an Membership , `yes`or`no` : "))
            if uuu == "yes":
                previous = str(input("Enter your previous Memebership ID : "))
                if previous == "memberayan789":
                    change = str(input("You Change your Membership ID `yes` or `no`: "))
                    if change == "yes":
                        print(
                            " `Your Membership ID should be combination of Charecters, Numbers, Spacial Charecters` "
                        )
                        newMID = str(input("Please Enter your new Membership ID: "))
                        print(f"Your new Membership ID is ,{newMID} ")
                        print("Save")
                    elif change == "no":
                        print("EXIT")
                        break
                    else:
                        print("Please! choice a predefind option. ")
                        break
                else:
                    print("Incorrect Membership ID! Please try again.")
                    break
            elif uuu == "no":
                print(
                    " `Your Membership ID should be combination of Charecters, Numbers, Spacial Charecters` "
                )
                createNewM = str("Enter Your Membership ID: ")
                print(f"Your Customer ID is,{createNewM} don't forget it !")
                print("Save")
            else:
                print("Please! choice a predefind option.")
                break
        elif choice == "3":
            print("EXIT")
            break
        else:
            print("Please! Select a predefind choice.")
            break


def issue():
    print("Any issue?")
    yesorno = str(input(" `yes` or `no`: "))
    if yesorno == "yes":
        print("If you facing anyproblem, please go to our website, name in below!")
        print("MyHpgas.in")

    elif yesorno == "no":
        print("`EXIT`")
    else:
        print("Please! choice a predefind option.")


# CALL {}
print("{````~ WELCOME TO HP ANYTIME ~````}")
while True:
    choice = str(
        input(
            " [1] `BOOKING CYLINDER` \n [2] `FORGOT PASSWORD OR REGENERATE PASSWORD` \n [3] `CREATE NEW ACCOUNT  OR MEMBERSHIP` \n [4] `ISSUE` \n [5] `HELP`\n [6] `EXIT` \n ```ENTER YOUR CHOICE``` \n >>> "
        )
    )
    if choice == "1":
        CID = str(input("Enter your CID: "))
        Password = str(input("Enter your password: "))
        cb = cybooking(CID, Password)
        print(cb)
    elif choice == "2":
        o = repass()
        print(o)
    elif choice == "3":
        asho = createAcc()
        print(asho)
    elif choice == "4":
        ola = issue()
        print(ola)
        break
    else:
        print("ERROR!!! 'Incorrect Choice' Please! choice a predefind option.")


# Look,
"""Something Wrong!"""
"""Code Pending"""
"""Incomplete"""
"""Try to better"""
