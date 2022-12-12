# Abstraction=need to know basis
# Encapsulation
# Polymorphism
# Inhertiance

student1={
    'name':'Jatin',
    'marks':50
}
student2={
    'name':'Samarth',
    'marks':100
}

# python object can have multiple traits
# -callable 
# - iterable 
# -contextable 

class person:
    pass
p= person()
print(p)
print(hex(id(p)))

def sq(a):
    print(a**2)

class Person:
    name ="jatin"
    def say_hi(self):
        print(f"Hello Everyone | I am {self.name}")

p=Person()
p.say_hi()
Person.say_hi(p)