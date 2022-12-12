def show_loading():
    for i in range(3):
        print(show_loading)


a = 5
b = 7
print(a+b)
show_loading

print(a-b)
show_loading

print(a*b)
show_loading

def sheldon_knock(name):
    for i in range(3):
        print("knock knock knock", name)
sheldon_knock("leanord")

def sheldon_knock(name,times = 3):
    for _ in range(times):
        print("knock knock knock",name)

def add(a,b):
    return a+b

a = add(1,2)    
print(a)