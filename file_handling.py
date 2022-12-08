# open - reading writing and creating files
# inputs - filename, mode - r, creating

# mode = 'r', r+ - both reading and writing, w - overwrite exisiting file
# close() - close function

# with open() - closes file automatically

# pass as binary - rb. rb+, wb, ab

# file = open('test.txt', mode='r')

# data = file.readline()

# print(data)

# file.close()

with open('test.txt', mode='r') as file:
    data = file.readline()
    print(data)

list = [1,2,3,4]

# list[4] = 5

list.insert(0,0)


