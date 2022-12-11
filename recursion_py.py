# used to solve problems that can be broken into smaller problems

# function that calls itself
# similar to a for loop

# looping solution
def find_factorial_by_looping(n):
    if n<0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial*i
        return factorial

print(find_factorial_by_looping(5))

# recursive solution
def find_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)

print(find_factorial_recursive(5))


# advantages -------------->
# neater code
# sub-problems
# easy sequences

# disadvantages ----------->
# hard to follow
# inefficient memory
# diffcult to debug