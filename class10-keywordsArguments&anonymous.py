def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(1,2,3)

def fun(a,b,c):
    print(a)
    print(b)
    print(c)
func(c=1,a=2,b=3)

def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,4,5)

def func(**k):
    print(k)
func(name="Jatin")

x = lambda a,b : a*b
print(x(1,2))