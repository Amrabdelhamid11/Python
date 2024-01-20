#####################CALCULATOR##########
num1=float(input("please,insert the first number  "))
opreator=input("{+ or - or * or / or ^ }")
num2= float (input("please, insert the second number"))
if opreator== "+":
    print(num1+num2)
elif opreator== "-":
    print(num1-num2)
elif opreator== "*":
    print(num1*num2)
elif opreator== "/":
    print(num1/num2)
elif opreator== "^":
    print(num1**num2)
else :
    print("error")
