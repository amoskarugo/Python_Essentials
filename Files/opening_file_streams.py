import sys
import errno
from os import  strerror




try:
    stream = open(file= "/home/amoh/Documents/tweeter.txt", mode='r', encoding="UTF-8")
except Exception as exc:
    print("cannot open the file", exc)



#open - if succesful returns a stream object otherwise an exception(e.g FileNotFoundError if the value you are going to read does not exist
#file - first param specifies the name of the file to be associated with the stream
#mode - specifies open mode
#encoding- specifies the encoding type
#the opening must be the very first operation performed on the stream

"""
Opening the streams: modes
1. r - open mode: read, file must exist
2. w -  open mode: write - opened in write mode, if file doesn't exist its created 
- if it exists will be truncated to length zero(erased)
-if creation is not possible the open function raises an exception

3. a - open mode: append
- the stream will be opened in append mode;
-the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; if it exists the virtual recording head
-will be set at the end of the file (the previous content of the file remains untouched).

4. r+ - open mode: read and update
- the stream will be opened in read and update mode;
- the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception;
- both read and write operations are allowed for the stream.
5. w+ open mode: write and update
- the stream will be opened in write and update mode;
- the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created; the previous content of the file remains untouched;
- both read and write operations are allowed for the stream.
"""

#read() method - read read all the contents at once when there is no argument passsed to it
#therefore, is not suitable for reading a terabyte-long file as it may corrupt your OS
try:
    counter  = 0
    _file = open("/home/amoh/Documents/tweeter.txt")
    ch = _file.read(1)
    while ch != "":
        counter += 1
        ch = _file.read(1)
    _file.close()
    print("characters read", counter)
except Exception as e:
    print("an error occurred", strerror(e.errno))

#readline() method
#treats the files content as a set of lines not a bunch of characters
#the method tries to read a complete set of line ot text from the file and returns it as a string in the case of success

try:
    char_counter  = line_counter = 0
    _file = open("/home/amoh/Documents/tweeter.txt")
    line = _file.readline()
    while line != "":
        line_counter+= 1
        for ch in line:
            print(ch, end='')
            char_counter += 1
        line = _file.readline()
    _file.close()
    print("characters read in file", char_counter)
    print("lines read in file", line_counter)
except Exception as e:
    print("an error occurred", strerror(e.errno))

#readlines() method
#treats text file as a set of lines
#The readlines() method, when invoked without arguments, tries to read all the file contents, and returns a list of strings, one element per file line.
#The maximum accepted input buffer size is passed to the method as its argument.
try:
    _file = open("/home/amoh/Documents/tweeter.txt")
    line = _file.readlines()
    print(line)

except Exception as e:
    print("an error happened", strerror(e.errno))


#Dealing with text files: write()


try:
    file = open('/home/amoh/Documents/write.txt', 'wt') # A new file (newtext.txt) is created.
    for i in range(10):
        s = "line #" + str(i+1) + "\n"
        for char in s:
            file.write(char)
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


#bytearray
#Before we start talking about binary files, we have to tell you about one of the specialized classes Python uses to store amorphous data
#Amorphous data is data which have no specific shape or form – they are just a series of bytes.
data  = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('/home/amoh/Documents/file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

#How to read bytes from a stream
#Reading from a binary file requires the use of a specialized method name readinto(),
#as the method doesn't create a new byte array object, but fills a previously created one with the values taken from the binary file.
"""
Note:

- the method returns the number of successfully read bytes;
- the method tries to fill the whole space available inside its argument; 
if there are more data in the file than space in the argument, the read 
operation will stop before the end of the file; otherwise, the method's 
result may indicate that the byte array has only been filled fragmentarily
(the result will show you that, too, and the part of the array not being used by the newly read contents remains untouched)

"""


#Character frequency histogram

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
try:
    file = open("/home/amoh/Documents/amoh.txt", "rt")
    for line in file:
        for char in line:
            # If it is a letter...
            if char.isalpha():
                # ... we'll treat it as lower-case and update the appropriate counter.
                counters[char.lower()] += 1
    file.close()
    # Let's output the counters.
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
