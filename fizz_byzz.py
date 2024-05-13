num1=input("Enter the limit :")
num2=int(num1)
for num in range(1,num2+1) :
    if num%3==0 and num%5==0 :
        print("FizzByzz")
    elif num%3==0 :
        print("Fizz")
    elif num%5==0 :
        print("Byzz")
    else :
        print(num)
