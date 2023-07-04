#python generator is a piece of specialized code able to produce a series of values
#and to control the iteration process

#You may not realize it, but you've encountered generators many, many times before. Take a look at the very simple snippet:
for i in range(5):
    print(i, end=" ")
    if i == 4:
        print()
#The range() function is, in fact, a generator, which is (in fact, again) an iterator.
#a function returns one, well-defined value - it may be the result of a more or less complex evaluation of something
#a generator returns a series of values, and in general, is (implicitly) invoked more than once
#in the example above the range generator is invoked 6 times, providing five subsequent values from zero to
#four and finally signalling tha the series is complete

"""
the iterator protocol is a way in which an object should behave to conform to the rules imposed
by the context of the for and in statements
- an object conforming to the iterator protocol is called an iterator

an iterator must provide two methods
- __iter__() which should return the object itself and which is invoked once(need for python to successfully
start the iteration)
- __next__() intended to return the next value of the desired series - it will be invoked by the for/in statements
in order to pass through the next iteration; if there are no more values to provide the method should raise the
StopIteration exception
 
 """


class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object:
    print(i)
