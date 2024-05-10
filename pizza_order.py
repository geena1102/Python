print("PIZZA ORDER PROGRAM")
size=input("Enter size of pizza(S/M/L)")
price=0
if size=='s' or size=='S' :
    price=price+100;
    print("Small pizza price is 100 Rs")
elif size=='m' or size=='M' :
    price=price+200
    print("Medium pizza price is 200 Rs")
else :
    price=price+300
    print("Large pizza price is 300 Rs")
add=input("Do you want pepperoni (y/N)?")
if add=='y' or add=='Y' :
    if size=='S' or size=='s' :
        price=price+30
    else :
        price=price+50
extra_cheese=input("Do you want extra cheese(Y/N)")
if extra_cheese=='y' or extra_cheese=='Y' :
    price=price+20
print(f"Total bill amount is : {price}")


