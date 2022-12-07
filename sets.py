set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
# sets don't allow duplicate values
# set_a.add(6)
# # set_a.remove(2)
# set_a.discard(2)

# both below work in the same way
# all values in both sets
print(set_a.union(set_b)) 
print(set_a | set_b)

# sets are mutable

# intersection - values appearing in both sets
print(set_a.intersection(set_b))
print(set_a & set_b)

# difference - values in 1st set not in second set
print(set_a.difference(set_b))
print(set_a - set_b)

# symmetrical difference - values in 1st set not in 2nd set and values in 2nd set not in 1st set
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

print(set_a)

# set is a collection of unordered list
# set is not a sequencee
print(set_a[0])
