# scoping - prevents unwanted changes in your code

# local scope
# enclosing - access local and nexted variables
# global scope - 

my_global = 10

def fn1():
    def fn2():
        enclosed_v = 8

    local_v = 5
    print(my_global)

fn1()
print(local_v)
# built-in scope - reserved key words
# can be accessed from the outermost and innermost scopes

#  LEGB



