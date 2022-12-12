a=[1,2,3,4]
print(a)
b=[1,'jatin','3',4]
print(b)

print(a[-1])


a.insert(1,100)
a.append(200)

a=[1,2,8,4,6]
a.pop()
print(a)

a.remove(1)

print(sorted(a))

a=[1,2,3,4]
for x in map(lambda x:x**2,a):
    print(x)

print(",".join("jatin",'samarth'))   