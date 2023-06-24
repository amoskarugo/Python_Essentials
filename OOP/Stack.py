#__init__ its a constructor function
#it has to be named in astrict way
#its invoked implicitly
"""
class stack:
    def __init__(self):
        print("Hi")
"""
#has atleast one parameter, the obligatory parameter is usually named self
class Stack:
    def __init__(self):
        self.__stack_list = []#two underscores before the name makes it private

    """
    both pop and push functions have self a parameter, it plays the same role as the first constructor
    parameter
    it allows the method to access entities(properties and activities/methods) carried out by the
    actual object
    everytime python invokes a method it implicitly sends the current object as the first argument 
    """
    def push(self, val):
        self.__stack_list.append(val)
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
    



#creating a subclass
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    def get_sum(self):
        return self.__sum
stack_object = AddingStack()   
for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())