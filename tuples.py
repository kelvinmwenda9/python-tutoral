# tuples 
my_tuple = (1, "strings", 4.5, True)
# tuples can be declared without parentheses

print(type(my_tuple))

print(my_tuple.count('strings')) 
# gives index position of tuple
# tuples start with 0 index
print(my_tuple.index(4.5))

for x in my_tuple:
    print(x)

# tuples as immutable

my_tuple[0] = 5