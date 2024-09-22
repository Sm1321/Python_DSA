import sys
l1 = []


print("initial size",sys.getsizeof(l1))


print('--'*10)
for i in range(0,17):
    l1.append(i)
    print(f"{i}-->{sys.getsizeof(l1)}")

'''
#Array
1.Array was fixed in size
2.Homogenous ,only a single Type Allowed
'''

l1 = []
a = 1
l1.append(1)

print(id(1))
print('----'*5)
print(id(a))
print('----'*5)
print(id(l1[0]))

