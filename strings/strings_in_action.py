#comparing strings
#Python strings can be compared using the same set of operators which are in use in relation to numbers.
# ==, !=, >, >=, <, <= operators all compare strings
'alpha' == 'alpha'
'alpha' != 'Alpha'

#both comparisons give True as a result

#When you compare two strings of different lengths and the shorter one is identical to the beginning of the longer one, the longer string is considered greater.
'alpha' < 'alphabet'#The relation is True.


#String comparison is always case-sensitive (upper-case letters are taken as lesser than lower-case ones).
'beta' > 'Beta' #The expression is True:

#if a string contains digits only, it's still not a number. It's interpreted as-is, like any other regular string, and its (potential) numerical aspect is not taken into consideration in any way.
'10' == '010'
'10' > '010'
'10' > '8'
'20' < '8'
'20' < '80'

#output
"""
False
True
False
True
True
"""
#Comparing strings against numbers is generally a bad idea
#The only comparisons you can perform with impunity are these symbolized by the == and != operators. The former always gives False, while the latter always produces True.
#Using any of the remaining comparison operators will raise a TypeError exception
'10' == 10
'10' != 10
'10' == 1
'10' != 1
'10' > 10
#output
"""
False
True
False
True
TypeError exception
"""

#SORTING
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)#new list is created

print(first_greek)
print(first_greek_2)

print()

second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()#no new list is created: sorts the string in situ
print(second_greek)

#string vs numbers
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

# str() to convert numbers to string
#int() or float() to convert a number string to int or float

