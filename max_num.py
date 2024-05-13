num = input("Enter numbers separated by spaces")
s_num = num.split()
max = 0
print("The list of num is",s_num)
#print(type(max))
for i in s_num :
    j=int(i)
    if j > int(max) :
        max=i
print("The max num is",max)

