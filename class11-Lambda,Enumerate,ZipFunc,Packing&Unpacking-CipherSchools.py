
names=['jatin', 'aaransh','shubham']
for name in enumerate(names):
    print(name)

for i,name in enumerate(names):
    print(i,"-",name)


scores=[50,60.90,70]

for name,score in zip(names,scores):
    print(name,"-",score)
