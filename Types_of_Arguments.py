#POSITIONAL ARGUMENT
def greet(name,dept) :
    print(f"Hello {name}")
    print(f"Are you frpm {dept} department")
greet("cs",'Geena')

#KEYWOD ARGUMENT
def greet(name,dept) :
    print(f"Hello {name}")
    print(f"Are you frpm {dept} department")
greet(dept="cs",name='Geena')

#DEFAULT ARGUMENT
def greet(name,subject,dept="CS") :
    print(f"Hello {name}")
    print(F"Do yo teach {subject} ")
    print(f"Are you frpm {dept} department")
greet("Geena","Python")

#ARBITRARY ARGUMENTS

def add(*numbers) :
    c=0
    for i in numbers :
        c=c+i
    print(f"Sum is {c}")
add(3,2,1)
add(4,3,1)
