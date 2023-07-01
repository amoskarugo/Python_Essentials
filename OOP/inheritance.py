#The Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes;
#
#The LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time;
#The TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes.
class Vehicle:
    pass
 
 
class LandVehicle(Vehicle):
    pass
 
 
class TrackedVehicle(LandVehicle):
    pass


#issubclass()
#issubclass(ClassOne, ClassTwo)
#The function returns True if ClassOne is a subclass of ClassTwo, and False otherwise.
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()

#isinstance()
#an object is an incarnation of a class.
#This means that the object is like a cake baked using a recipe which is included inside the class.
#isinstance(objectName, ClassName)
#The function returns True if the object is an instance of the class, or False otherwise
#Being an instance of a class means that the object (the cake) has been prepared using a recipe contained in either the class or one of its superclasses

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()


#The is operator
#he is operator checks whether two variables (object_one and object_two here) refer to the same object
class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)


#How Python finds properties and methods
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)
#there is a class named Super, which defines its own constructor used to assign the object's property, named name.
#the class defines the __str__() method, too, which makes the class able to present its identity in clear text form.
#the class is next used as a base to create a subclass named Sub. The Sub class defines its own constructor, 
#which invokes the one from the superclass. Note how we've done it: Super.__init__(self, name).
#we've explicitly named the superclass, and pointed to the method to invoke __init__(),providing all needed arguments.
#we've instantiated one object of class Sub and printed it
# As there is no __str__() method within the Sub class, the printed string is to be produced within the Super class
#This means that the __str__() method has been inherited by the Sub class.

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)
#the super() function, which accesses the superclass without needing to know its name:
#super() function creates a context in which you don't have to (moreover, you mustn't) pass the self argument to the method being invoked
#Note: you can use this mechanism not only to invoke the superclass constructor, but also to get access to any of the resources available inside the superclass.

# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)

#Note: the existence of the supVar variable is obviously conditioned by the Super class constructor invocation. 
#Omitting it would result in the absence of the variable in the created object (try it yourself).

#Python's behavior.
#When you try to access any object's entity, Python will try to (in this order):
# - find it inside the object itself;
# - find it in all classes involved in the object's inheritance line from bottom to top;
#If both of the above fail, an exception (AttributeError) is raised.

# three-level inheritance line
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())



#MULTIPLE INHERITANCE
#Multiple inheritance occurs when a class has more than one superclass
class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
 
 
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
 
 
class Sub(SuperA, SuperB):
    pass
 
obj = Sub()
 
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

#overriding.
class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())
#Both, Level1 and Level2 classes define a method named fun() and a property named var.
#Does this mean that the Level3 class object will be able to access two copies of each entity? Not at all.
#The entity defined later (in the inheritance sense) overrides the same entity defined earlier
#This feature can be intentionally used to modify default (or previously defined) class 
#behaviors when any of its classes needs to act in a different way to its ancestor.
#We can also say that Python looks for an entity from bottom to top,
#and is fully satisfied with the first entity of the desired name


class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())

"""
The Sub class inherits goods from two superclasses, Left and Right (these names are intended to be meaningful).
There is no doubt that the class variable var_right comes from the Right class,
This is clear. But where does var come from? Is it possible to guess it?
and var_left comes from Left respectively.
The same problem is encountered with the fun() method 
will it be invoked from Left or from Right? Let's run the program
This proves that both unclear cases have a solution inside the Left class.
Is this a sufficient premise to formulate a general rule? Yes, it is.

We can say that Python looks for object components in the following order:
#inside the object itself;
#in its superclasses, from bottom to top;
#if there is more than one class on a particular inheritance path, Python scans them from left to right.

"""

#How to build a hierarchy of classes

#POLYMORPHISM

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()