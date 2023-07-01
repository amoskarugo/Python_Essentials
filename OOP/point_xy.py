import math

#Points on a plane

"""
Each point located on the plane can be described as a pair of coordinates customarily called x and y.
write a Python class which stores both coordinates as float numbers. 
objects of this class will evaluate the distances between any of the two points situated on the plane.

This is how you imagine the class:
-it's called Point;
-its constructor accepts two arguments (x and y respectively), both of which default to zero;
-all the properties should be private;
-the class contains two parameterless methods called getx() and gety(), 
which return each of the two coordinates (the coordinates are stored privately, 
so they cannot be accessed directly from within the object);
-the class provides a method called distance_from_xy(x,y), 
which calculates and returns the distance between the point stored 
inside the object and the other point given as a pair of floats;
-the class provides a method called distance_from_point(point), 
which calculates the distance (like the previous method), but the other point's 
location is given as another Point class object;
"""
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x - x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())
    
#embed the Point class inside another class
#put three points into one class, which will let us define a triangle. 
#The new class will be called Triangle and this is what we want:
"""
-the constructor accepts three arguments – all of them are objects of the Point class;
-the points are stored inside the object as a private list;
-the class provides a parameterless method called perimeter(), 
which calculates the perimeter of the triangle described by the three points; 
the perimeter is the sum of all the lengths of the legs 
(we mention this for the record, although we are sure that you know it perfectly yourself.)
"""


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        per = 0
        for i in range(3):
            per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        return per
    

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())