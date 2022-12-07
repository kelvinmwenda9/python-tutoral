# synatx - caused by developer
# exceptions - known errors that need to be handled
# happening during execution
# a = 5/0

# exception handling

def divide_by(a, b):
    return a / b


try:
    ans = divide_by(40,0)
except Exception as e:
    print('something went wrong')

# print(divide_by(5,0))

