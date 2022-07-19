a = [100, 200, 300, 400, 500]
print(' '.join(map(str, a)))

a.insert(1, 350)
print(a)

a.sort()
print(*a)

a.sort(reverse = True)
print(a)


#Yoni
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

#Yoni
aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList)