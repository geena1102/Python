heights=input("Enter heights separated by commas")
#print(heights)
s_height=heights.split(',')
sum=0
length=len(s_height)
print(s_height)
for i in s_height :
    sum=sum+int(i)
avg=round(sum/length)
print(f"The average height is {avg}")
