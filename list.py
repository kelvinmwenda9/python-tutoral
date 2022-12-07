# sequence of one or more different or similar data types
# dynamic array that can hold any data type

list1 = [1,2,3,4]

print(list1[2])

list2 = ['A','B','C','D']
list3 = ['hello', 1, True, 48.22]

list4 = [1,[2,3,4],5,6]
print(list4[1][2])

list1.insert(len(list1), 6)
print(list1)

list1.append(7)

print(list1)

list1.extend([8,9,10])
print(list1)

# remove item from list using pop
list1.pop(8)
print(list1)

del list1[7]
print(list1)

# iterate through list
for x in list1:
    print('Value ', x)


