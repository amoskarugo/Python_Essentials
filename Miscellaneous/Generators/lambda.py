#programmers use lambda function to simplify the code, to make it clearer to understand
#lambda is a function without a name(anonymous fuction)


#lambda function declaratio => lamdba parameters: expression
#returns the value of the expression when taking into account the value of the lambda argument


two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 2):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
#how to use lambdas and what for
#The most interesting thing about lambdas is that you can use them in their pure form  -
#as anonymous parts of code intended to evaluate a result.
#Imagine that we need a function (we'll name it print_function) which prints the values -
#of a given (other) function for a set of selected arguments.
#We want print_function to be universal – it should accept a set of arguments -
#put in a list and a function to be evaluated, both as arguments – we don't want to hardcode anything.

def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')


def poly(x):
    return 2 * x ** 2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

"""
The print_function() function takes two parameters:
- the first, a list of arguments for which we want to print the results;
-the second, a function which should be invoked as many times as the number of values that are collected inside the first parameter.
Note: we've also defined a function named poly()– this is the function whose values we're going to print.
-The name of the function is then passed to the print_function() along with a set of five different arguments – 
the set is built with a list comprehension clause.
"""
#Can we avoid defining the poly() function, as we're not going to use it more than once?
#Yes, we can – this is the benefit a lambda can bring.
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep='')


print_function([x for x in range(-2, 3)], lambda x: 2 * x ** 2 - 4 * x + 2)

#Lambdas and the map() function
#map(function, list)
"""
- takes two arguments: a function and a list
"""
list_1 = [x for x in range(5)] #list comprehension
list_2 = list(map(lambda x: 2 ** x, list_1)) #map returns a generator and use list comprehension to create list2
print(list_2)

for x in map(lambda x: x * x, list_2):# looping through the generator
    print(x, end=' ')
print()

# Lambdas and the filter() function
#Another Python function which can be significantly beautified by the application of a lambda is filter().
# it filters its second argument while being guided by directions flowing from the function specified as the first argument
#(the function is invoked for each list element, just like in map()))
#The elements which return True from the function pass the filter – the others are rejected.
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

#closures

#closure is a technique which allows the storing of values in spite of the fact that the context in which they
#have been created does not exist anymore
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc

    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
