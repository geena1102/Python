name1=input("Name of girl")
name2=input("Name of boy")
name=name1+name2
l_name=name.lower()
t = l_name.count('t')
r = l_name.count('r')
u = l_name.count('u')
e = l_name.count('e')
true=t+r+u+e


l = l_name.count('l')
o = l_name.count('o')
v = l_name.count('v')
e = l_name.count('e')
love=l+o+v+e

love_score=int (str(true)+str(love))
if love_score < 10 or love_score> 90  :
    print(f"Your love score is {love_score} and you go together like coke and mentos")
elif love_score >=40 and love_score <=50 :
    print(f"Your love score is {love_score} and you are alright together")
else:
    print(f"Your love score is {love_score}")