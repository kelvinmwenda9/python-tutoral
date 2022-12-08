# synatx - caused by developer
# exceptions - known errors that need to be handled
# happening during execution
# a = 5/0

# exception handling

def divide_by(a, b):
    return a / b


# try:
#     ans = divide_by(40,0)
# except Exception as e:
#     print('something went wrong', e)
#     print(e.__class__)    # prints the exceptions class


try:
    ans = divide_by(40,0)
except ZeroDivisionError as e:
    print(e, 'number is not divisible by zero')
    print(e.__class__)    # prints the exceptions class
except Exception as e:
    print("this is a generic exception", e)

# print(divide_by(5,0))

