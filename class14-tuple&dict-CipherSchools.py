a=(1,2,3,4)
print(a)

def func(*a):
    print(type(a))

func()

a=1,2,4,5,6,7
print(type(a))

a={
    'name':'Jatin',
    1: "something",
    (1,2):"tuple key"
}
print(a['name'])
print(a[1])

key="name"
print(a.get(key))

print(a.values())

for x in a.items():
    print(x)

for x in a:
    print(x)

print(list(a.items()))
print(list(a.keys()))
