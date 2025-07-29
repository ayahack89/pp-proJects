#Make a calculater using python.
print('''
'+' Additition , '-' Subtraction ,'*' Multiplication ,'/' Division 
,'**' Power , '//' Float division ''')
num1=int(input("Enter the first value: "))
op=input("Enter the operator: ")
num2=int(input("Enter the second value: "))
if (op=="+"):
    print(num1+num2)
elif (op=="-"):
    print(num1-num2)
elif (op=="*"):
    print(num1*num2)
elif (op=="/"):
    print(num1/num2)
else:
    print("ERROR>>>invalid operator.")