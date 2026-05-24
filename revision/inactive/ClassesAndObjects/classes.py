'''
class
attributes
objects
class objects
__init__() method
types of methods
types of variables

class:
    class is a description of an object
    it defines various attributes of an object

    defining a class is creating a data type

encapsulation:
    an act of combining properties and methods related to same object is known as encapsulation
    class is a way to implement encapsulation
  
attributes:
    attributes are member variables and member function  

objects:
    objects is an instance of a class
    objects are of two types:
        class object
        instance object

    t1=Test()
    t2=Test()
    t1 and t2 are are instance objects of Test class

Class Object
    Test vs Text()


    one class has exactly one class object but can have any number of instace objects

Class Test:
    t1=Test()
    t2=Test()
    t3=Test()

    class object variables ==> static variables
    instance object variables
'''

# l1=[10,20,30]
# l1.append(40)
# print(l1)

class Test:
    x=5
    def f1():
        print("Hello World")

t1=Test()
t2=Test()
