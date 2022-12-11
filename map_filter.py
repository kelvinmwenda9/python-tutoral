# process a list with map and filter functions

menu = ['reverse', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']

# print all coffees that start with letter c
# arguments - function, articles that will be passed in that function

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = map(find_coffee, menu)


print(map_coffee) # map object as output

for x in map_coffee:
    print(x)
    # all without c's are printed as none


# filter function

filter_coffee = filter(find_coffee, menu)

print(filter_coffee)

for x in filter_coffee:
    print(x)

# maps - take all objects in a list and applies a function
# filters - does the same as a map, but takes the results 
# # and creates a new list with only the true values

# summary - map() returns every item in an iterable and filter() returns values if True.


a = [[96],[96]]

print(''.join(list(map(str,a))))
# ans = [96][96]

# map() and filter() are built-in

z = ["alpha", "bravo", "charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)
# ans - ['aa', 'bb', 'cc']

