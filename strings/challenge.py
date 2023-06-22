#write your own function which behaves almost exactly like the original split() method
#it should accept exactly one argument – a string;
#it should return a list of words created from the string, divided in the places where the string contains whitespaces;
#if the string is empty, the function should return an empty list;


def mysplit(string):
    lst = []
    word = ""
    for ch in string:
        if ch.isspace():
            if word != "":
                lst.append(word)
            word = ""
            continue
        word += ch
    return lst
# test cases
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

#output
"""
['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the']
['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the']
[]
['abc']
[]
"""