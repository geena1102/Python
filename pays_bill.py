import random
names=input("Enter the names separated by commas")
names_split=names.split(",")
#print(names_split)
length=len(names_split)
r=random.randint(0,length-1)
#print(f "{names_split[r]} will pay the bill")
print(f"{names_split[r]} will pay the bill")