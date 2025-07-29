#Goood morning sir.
def goodday(a,rep,w):
    if (a=='8am'):
        return print("Good morning sir. Have a nice day.")
    elif (a=='2pm'):
        return print("Good after noon , now its your lunch break sir, please complete your lunch.")
    elif (a=='4pm'):
        
        if (rep=="very Good"):
            return print("WoW!")
        elif (rep=="good"):
            return print("oooo")
        elif (rep=="sad"):
            return print("Why!")
        else:
            return print("Please ! behave your self. Are you sceared?_!.")
    elif (a=='9pm'):
        return print("Its your dinner time, please complete your dinner.")
    elif (a=='11pm'):
        return print("Good night darling! sweet dream!")
    else:
        return print("Error")
a = (input("Enter time: "))
rep=input("Good evening sir_How abuot your day? ")
w=int(input("What's the actuall reson why you are so sad ! tell me I can fix that:"))
x=goodday(a,rep,w)
print(x)


        
