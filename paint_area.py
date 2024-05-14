import math
def paint(height,width,cover) :
    area=height*width
    no_of_paints=math.ceil(area/cover)
    print(f"No of paint neded is {no_of_paints}")
h=int(input("Enter height"))
w=int(input("Enter width"))
coverage=7

paint(width=w,height=h,cover=coverage)
