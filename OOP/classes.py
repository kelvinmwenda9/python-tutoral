class MyClass:
    a = 5
    # print('Hello')

    def hello(self):    # doesn't work when self is not included
        print('hello world')

myc = MyClass()

print(myc.a)
print(MyClass.a)
print(myc.hello())

# instatiation process
# class definition - creating a new instance - initializing the new instance

# classes - perform 2 operations
# attribute reference and instantiation

# pass - allows the program to continue execution without impacting any functionality or flow


# abstract class - class for which you cannot create an instance, python doesn't supprot abstraction directly -> import module
# methods need to be defined before implemented

# Abstract class acts only as a base class for other classes to derive from it.
# Abstract classes may or may not cannot abstract method definitions.
# Python makes use of class abc as a superclass to implement Abstraction.
# Python makes use of the abc class to implement abstraction.
# The name of the function required inside the abc module is abstract method.

# advantages of abstract classes
# ability to hide the details of implementation without sacrificing functionality 
# 2 ways -> implement in child class -> super class()

# import abc
# creat inheriting class -> pass abc module
# import abstract method decorator -> a fun that takes another fun as argument and gives a new fun as result
# @
# call abstract method

# import abc and method
# define abc method
# create sub-class
# implementation
# create instances

# Before implementing an abstract method, you need to import the abstract base class module, and create a class that inherits it. 



