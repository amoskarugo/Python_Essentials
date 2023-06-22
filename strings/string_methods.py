# The capitalize() method
#creates a new string filled with characters taken from the source string
#modifies the string  in the following ways
"""-if the first character is a letter it is converted to uppercase
    - all remaining letters from the string will be converted to lower-case"""

#the original string is not changed in any way
#modified string is returned as the result
print("aBCD".capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())

#THE center() method
#makes a copy of the original string trying to center it inside a field of a specified width

#adding some spaces before and after the string
print('[' + 'alpha'.center(10) + ']')
#out put [  alpha   ]
#if the target field is too small to fit the original sreing is returned

print('[' + 'gamma'.center(20, '*') + ']') #two parameter variant of center()

#output => [*******gamma********]

#the endswith() method
#checks if the given string ends with the specified argument and returns True or False depending on check results
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

#The find() method
#similars to index() method
#does'nt generate an error for an argument containing non-existent substring(it returns -1)
#works with strings only- don't apply it to any other sequence
#NB: don't use find if you want want to check for a single char instead use in it's much faster

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))


print('kappa'.find('a', 2))# two parameter variant
#2nd argment specifies the index at which search will be started
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

print('kappa'.find('a', 1, 4))#3 parameter mutation of the find() method
print('kappa'.find('a', 2, 4))
#the 3rd argument points to the first index which won't be taken into consideration during the search


#the isalnum() method
#checks if the string contains only digits or alphabetical characters(letters), and returns
# True or False
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
# any string character that is not a letter or a digit causes the function to return false

t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

#output False, False, True

#the isalpha() method
#it's interested in letters only
print("Moooo".isalpha())
print('Mu40'.isalpha())
#output True, False

#the isdigit() method
#looks for digits only anything else it returns false
print('2018'.isdigit())
print("Year2019".isdigit())
#output True, False

#the islower() method
#accepts lower case letters only
print("Moooo".islower())
print('moooo'.islower())
#output  False, True

#the isspace() method
#identifies whitespace only
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
#output  true, true , false

#the isupper() method
#method is upper-case version of islower() method
#it concentrates on uppper-case letters only
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
#output false, false, true

# the join() method

#takes one argument as a list, all list elements must be strings(method raises a typeerror otherwise)
#elements will be joined into one string and the string from which the method has been invoked used as seperator
#newly created string returned as a result
print(",".join(["omicron", "pi", "rho"]))
#output => omicron,pi,rho

#the lower() method
#makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts, and returns the string as the result. Again, the source string remains untouched.
#does'nt take any parameters
print("SiGmA=60".lower())

#the lstrip() method
#returns a newly created string formed from the original one by removing all leading whitespaces.
print("[" + " tau ".lstrip() + "]")
#output =>[tau ]

print("www.cisco.com".lstrip("w.ci"))#one parameter version
#method does the same as its parameterless version, but removes all characters enlisted in its argument (a string), not just whitespaces:


#the replace() method
#2 parameter fuction
#returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print("This is it!".replace("is", "are", 1))#3 parameter
#The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.

#The rfind() method

#start their searches from the end of the string
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

#The rstrip() method
#Two variants of the rstrip() method do nearly the same as lstrips, but affect the opposite side of the string
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))


#The split() method
print("phi       chi\npsi".split())
#splits the string and builds a list of all detected substrings
#assumes that the substrings are delimited by whitespaces 
#If the string is empty, the resulting list is empty too.


#The startswith() method
#The startswith() method is a mirror reflection of endswith() – it checks if a given string starts with the specified substring.
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

#The strip() method
#The strip() method combines the effects caused by rstrip() and lstrip() – it makes a new string lacking all the leading and trailing whitespaces.
print("[" + "   aleph   ".strip() + "]")


#The swapcase() method
#The swapcase() method makes a new string by swapping the cases of all letters within the source string: lower-case characters become upper-case, and vice versa.
print("I know that I know nothing.".swapcase())

print()

#The title() method
#The title() method performs a somewhat similar function – it changes every word's first letter to upper-case, turning all other ones to lower-case.
print("I know that I know nothing. Part 1.".title())

print()
#The upper() method
#upper() method makes a copy of the source string, replaces all lower-case letters with their upper-case counterparts, and returns the string as the result.
print("I know that I know nothing. Part 2.".upper())

