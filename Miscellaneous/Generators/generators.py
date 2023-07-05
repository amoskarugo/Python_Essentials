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
#SUMMARY
"""
1. An iterator is an object of a class providing at least two methods (not counting the constructor):
- __iter__() is invoked once when the iterator is created and returns the iterator's object itself;
- __next__() is invoked to provide the next iteration's value and raises the StopIteration exception
 when the iteration comes to and end.

2. The yield statement can be used only inside functions. The yield statement suspends function execution
 and causes the function to return the yield's argument as a result. Such a function cannot be invoked in
  a regular way – its only purpose is to be used as a generator (i.e. in a context that requires a series 
  of values, like a for loop).
  
  3. A conditional expression is an expression built using the if-else operator. For example:
  print(True if 0 >= 0 else False)

4. A list comprehension becomes a generator when used inside parentheses (used inside brackets, 
it produces a regular list). For example:
for x in (el * 2 for el in range(5)):
print(x)

4. A lambda function is a tool for creating anonymous functions. For example:
def foo(x, f):
    return f(x)

print(foo(9, lambda x: x ** 0.5))
5. The map(fun, list) function creates a copy of a list argument, and applies the fun function to all of its elements,
 returning a generator that provides the new list content element by element. For example:
 
short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)

6. The filter(fun, list) function creates a copy of those list elements,
 which cause the fun function to return True. The function's result is a generator 
 providing the new list content element by element. For example:

short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)

7. A closure is a technique which allows the storing of values in spite of the fact that 
the context in which they have been created does not exist anymore. For example:

def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner


b_tag = tag('<b>')
print(b_tag('Monty Python'))


"""