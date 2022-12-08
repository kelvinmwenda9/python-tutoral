# read - entire content as string, int to return characters
# readline - singleline as string, specified number of characters
# readlines - entire file contents and returns as OL

# paths
# absolute - leading forward slash or drive label
# relative - don't contain path details to locatie file

with open('sample.txt', 'r') as file:
    # print(file.read(44))
    # data = file.readlines()
    # print(data)
    for x in file:
        print(x)

