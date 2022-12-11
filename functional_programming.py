# high
# function takes input - processes - sends output

# traditional - -->
# access global state
# modify global variables
# access local state
# change args

# pure - do the same things and return the same results no matter how many times they are called
# access local state
# otuput depends on iput

# functional programming is paradigm that uses functions for clean, consistent, maintainable code
# does not data outside the scope of the function
# standalone/independent

# functions are first class citizens, they have the same level of strings and numbers
# can be assigned as variables
# can be passed as an argument
# can be returned to its caller

# sorted function - list items in alphabetical order

# reverse function

coffees = ['espresso', 'latte', 'capuccino', 'macchiato', 'americano', 'decaf']

def reverse(str):
    return str[::-1]

reversed_coffees = map(reverse, coffees)

for x in reversed_coffees:
    print(x)

# pure functions - clean, easy to debug, extendable
# function that doesn't change or have any effect on a variable, data. list or set beyond it's own scope

# accept list as argument, original list intact, return new list

# benefits of pure functions ---------->
# knonw outcome
# consistent and reliable
# cache
# multi-threaded programs

