import random
a = []

for i in range(180):
    a.append(random.randint(1,5))

print('1: ',a.count(1))
print('2: ',a.count(2))
print('3: ',a.count(3))
print('4: ',a.count(4))
print('5: ',a.count(5))
