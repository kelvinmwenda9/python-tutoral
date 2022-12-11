# reverse a string in python

# two ways to reverse a string in python

# slice function

# str[start:stop:step] - extended slice syntax
# ### indexes through which the function manipulates the string
# The start and stopparameters are the indices between 
# which the function manipulates the string. 
# The stepparameter are the hops or jumps the function 
# makes while it traverses a given string.  

trial = 'reversal'

new_trial = trial[::-1] 
# string is traversed from the right, onde index position at a time

print(new_trial)

# -----------------------------------

# recursion to reverse a string

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
        # string is traversed from the front skipping the first character in every loop

str = 'reversal'
reverse = string_reverse(str)
print(reverse)