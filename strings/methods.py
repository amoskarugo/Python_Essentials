str1 = "a"
str2 = " "


print(chr(100))#chr () fuctions receives a code point value a returns the corresponding character
print(ord(str2))# ord () helps you to know a specific character's ASCII/UNICODE code point value
#ord () needs one-character string as its argument


#STRINGS AS SEQUENCES 


# #indexing strings

the_string = "silly jokes"
for ix in range(len(the_string)):
    print(the_string[ix], end=" ")
print()
# it is possible to index strings as is in lists but strings bounderies must be observerd

#iterating

for character in the_string:
    print(character, end=" ")
print()

#slices
vowel = "aeiou"
print(vowel[1:3])
print(vowel[3:])
print(vowel[-1])
print(vowel[-3:-1])
print(vowel[::2])
print(vowel[1::2])

#THE in AND not in OPERATOR

#the in operator => checks if its left argument(a string) can be found anywhere within the 
#right argument(another string)

#results amounts to True or False
#in operator
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
#not in operator

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


#python strings are immutable
#have not del or append() methods
#del alphabet[0] will raise an error

#THE min() and max() methods
string  = "berxyxzZ"
print(min(string)) # finds the minimum of the sequence passed as an argument
#the string must not be empty
#output => b has the lowest ascii code point value
print(max(string))#finds the maximum of the sequence passed as an argument 
#output => lower case z occupies the highest location on ascii table
#  

#The index() method

"""searches the sequence from the beginning, in order to find the first element
of the value specified in its argument.
the element searched for must occur in the sequence - its absence will cause a ValueError exception

"""
print("agdofYxnZndWmM".index("d"))


#The list() function
"""takes its argument(a string) and creates a new list containing all the sting's characters,
one per list element
NB: it's not strictly a string function
its able to create a new list from many other entities(e.g tuples and dictioneries)"""

print(list("abc"))
#output ['a', 'b', 'c' ]

#The count() method
#counts all the occurrences of the element inside the sequence
#absence of such element does not cause any eeror

print("abadfoedaa".count("a"))

#output 4
