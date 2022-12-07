# dict access values using keys
# dict is mutable

sample_dict = {1:'Coffee', 2:'Tea', 3:'Juice'}

print(sample_dict[2])

sample_dict[2] = 'Milk'
print(sample_dict)

del sample_dict[3]

print(sample_dict)

# iterate through dictionary using
# standard method, items(), Values()

my_d = {1:'Test', 'Name':'John'}

my_d[2] = 'Test 2'

# doesn't alow a duplicate key

print(my_d)

for x in my_d:
    print(x)

for key, value in my_d.items():
    print(str(key) + " : " + value)