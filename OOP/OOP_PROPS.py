#different objects of the same class may possess different set of properties
#each object carries its own set of properties - they don't interfere with one another in any way
#such variables(properties) are called instance variables
#instance suggests that they are closely connected to the objects

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
    def set_second(self, val):
        self.set_second = val

example_object1 = ExampleClass()
example_object2 = ExampleClass(2)
example_object2.set_second(3)

example_object3 = ExampleClass(4)
example_object3.third =  5

# print(example_object1.__dict__)
# print(example_object2.__dict__)
# print(example_object3.__dict__)

#python objects, when created, are gifted a small set of predefined properties and methods
#modifying an instance variable of any object has no impact on all the remaining objects
#instance variables are perfectly isolated from each other



#------------------------------------------------------------------------------------------

#this example is nearly the same as the previous one - difference we've added two
#underscores in front of them
#__ makes the variables private- becomes inaccessible from the outer world
#but the actual behavior in the code below is a bit complicate
#we are able to access and modify the outside the class
"""
python sees that you want to add an instance variable to an object and you're going to do it
inside any of the objects methods, it mangles the operation in the following way
-it puts a class name before your name
-it puts an additional underscore at the beginning
i.e _ExampleClass__first
the  name is now fully accessible from outside the class
"""
#the mangling won't work if you add a private instance variable outside the class code
#in this case it'll behave like any other ordinary property

class ExampleClass2:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass2()
example_object_2 = ExampleClass2(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass2(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


#CLASS VARIABLES
"""
# class variable is a property which exists in just one copy and is stored outside any object
NB: no instance variable that exists if there are no objects; a class variable exists in one copy 
even if there are no objects in the class
"""
#Class variables are created differently to their instance siblings
#accessing such a variable looks the same as accessing any instance attribute 
#class variables aren't shown in an object's __dict__
#a class variable always presents the same value in all class instances
#Mangling a class variable's name has the same effects as those you're already familiar with.
class ExampleClass3:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass3.counter += 1
 
 
example_object_1 = ExampleClass3()
example_object_2 = ExampleClass3(2)
example_object_3 = ExampleClass3(4)
 
print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)


#Checking an attribute's existence
#The object created by the constructor can have only one of two possible attributes: a or b.
#The below code will run into an error since there will be no an attribute named b
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)

#this how you can run it and escape the exception
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
 
 
example_object = ExampleClass(1)
print(example_object.a)
 
if hasattr(example_object, 'b'):
    print(example_object.b)