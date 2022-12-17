# Method resolution order

class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())


# types of inheritance

# simple inheritance
# multiple inheritance - one class inheriting from multiple classes

# multi-level inheritance - inheritance taking place in several levels

# hierarchical inheritance - subclasses inheriting from a parent class

# hybrid inheritance - mixes characteristics of the others

# developers solve this issue using MRO - MRO determines the order in which a given 
# method or attribute passed is searched
# determines the order in which a given method or attribute is passed through 
# in a search of the hierarchy of classes for its resolution or where it belongs

# the order of the resolution is called linearization of the class
# bottom to top -> left to right

# depth-first serarch algorithm

# c3 linearization algorithm
# which follows:
# - adheres to monotonicity
# - follows inheritance graph
# - visits super class after local classes


# finding MRO of a class
# MRO attribute
# mro()

class A:
    pass

class B(A):
    num = 9

class C(B):
    # MRO tells you quickly that class will inherit value from class B
    pass
print("======================")
print(C.mro())

# help() Help Function

print(help(C))