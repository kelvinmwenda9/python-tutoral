def sum_of(a, b):
    return a + b

print(sum_of(5,6))

# *args allows for multiple arguments to be passed
# you can pass any ammount of non- key values arguments
def sum_to(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_to(7,8,9,10))

# kwargs 
# can pass any amount of key value arguments
def sum_to(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_to(coffee=2.99, cake=4.55, juice=2.99))

# num = 30
# for x in num:
#     print(num)