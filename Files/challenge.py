from os import  strerror
import errno
"""
Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements:
the student's first name, the student's last name, and the number of points the student received during certain classes.
The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:

John     Smith    5
Anna     Boleyn   4.5
John     Smith    2
Anna     Boleyn   11
Andrew   Cox      1.5

Your task is to write a program which:

asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:

Andrew   Cox      1.5
Anna     Boleyn   15.5
John     Smith    7.0

Note:

- your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures;
encountering any data error should cause immediate program termination, and the error should be presented to the user;
- implement and use your own exceptions hierarchy – we've presented it in the editor; the second exception should be raised when a wrong line is detected,
 and the third when the source file exists but is empty
"""

# A base exception class for our code:
class StudentsDataException(Exception):
    pass


# An exception for erroneous lines:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# An exception for an empty file.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)



# A dictionary for students' data:
data = { }

file_name = input("Enter student's data filename: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Read the whole file into list.
    lines = f.readlines()
    f.close()
    # Is the file empty?
    if len(lines) == 0:
        raise FileEmpty()
    # Scan the file line by line.
    for i in range(len(lines)):
        # Get the i'th line.
        line = lines[i]
        # Divide it into columns.
        columns = line.split()
        # There shoule be 3 columns - are they there?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Build a key from student's given name and surname.
        student = columns[0] + ' ' + columns[1]
        # Get points.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Update dictionary.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Print results.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except WrongLine as e:
    print("Wrong line #" + str(e.line_number) + " in source file:" + e.line_string)
except FileEmpty:
    print("Source file empty")