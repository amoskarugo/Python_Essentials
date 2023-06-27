# a method is a function inside a class

class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()
    
#a method is obligated to have at least one parameter(self)
#self - it identifies the object for which the method is invoked
#while invoking the method no need to pass the argument self, python will do it for you
#self parameter is used to obtain access to the objects instance and class variables
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
 
 
obj = Classy()
obj.var = 3
obj.method()


#self is also used to invoke other object/class methods from inside the class
class Classy:
    def other(self):
        print("other")
 
    def method(self):
        print("method")
        self.other()
 
 
obj = Classy()
obj.method()

#If you name a method like this: __init__, it won't be a regular method – it will be a constructor.
#If a class has a constructor, it is invoked automatically and implicitly when the object of the class is instantiated.
"""
The constructor:

-is obliged to have the self parameter (it's set automatically, as usual)
-may (but doesn't need to) have more parameters than just self;
if this happens, the way in which the class name is used to
create the object must reflect the __init__ definition;
-can be used to set up the object, i.e., properly initialize its internal state, 
create instance variables, instantiate any other objects if their existence is needed, etc.

"""
#property name mangling applies to method names, too 
#Example
class Classy:
    def visible(self):
        print("visible")
 
    def __hidden(self):
        print("hidden")
 
 
obj = Classy()
obj.visible()
 
try:
    obj.__hidden()
except:
    print("failed")
 
obj._Classy__hidden()

#__name__ property shows the name of a class
# the __name__ attribute is absent from the objects - its exists only inside classes

#finding the name of a particular object, use type() function
class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

#__module__ it stores the name of the module which contains the definition of the class
class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)

#__bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.

#The order is the same as that used inside the class definition.
#Note: only classes have this attribute – objects don't.

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

#Reflection and introspection
"""
All these means allow the Python programmer to perform two important activities specific to many objective languages. They are:

-introspection, which is the ability of a program to examine the type or properties of an object at runtime;
-reflection, which goes a step further, and is the ability of a program to manipulate the values, properties and/or functions of an object at runtime.
"""
#Investigating classes

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
"""
This is how it works:

-line 1: define a very simple class...
-lines 3 through 10: ... and fill it with some attributes;
-line 12: this is our function!
-line 13: scan the __dict__ attribute, looking for all attribute names;
-line 14: if a name starts with i...
-line 15: ... use the getattr() function to get its current value; note: getattr() takes two arguments: an object, and its property name (as a string), and returns the current attribute's value;
-line 16: check if the value is of type integer, and use the function isinstance() for this purpose (we'll discuss this later);
-line 17: if the check goes well, increment the property's value by making use of the setattr() function; the function takes three arguments: an object, the property name (as a string), and the property's new value.
"""