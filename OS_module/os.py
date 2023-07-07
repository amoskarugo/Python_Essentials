import  os
#interacting with the operating system using python
#Getting information about the operating system
#os module provides a function called uname, which returns an object containing the following attributes:

"""
systemname — stores the name of the operating system;
nodename — stores the machine name on the network;
release — stores the operating system release;
version — stores the operating system version;
machine — stores the hardware identifier, e.g., x86_64.
"""

#print(os.uname())

#Creating directories in Python


#os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory") #change directory
print(os.listdir())#list directories in specified path equivalent to ls command in unix systems
print(os.getcwd())#current working directory
os.chdir("my_second_directory")
print(os.getcwd())

#Deleting directories in Python
#o delete a single directory, you can use a function called rmdir
#rmdir - directory must exist and it should be empty
os.mkdir("my_second_directory")
print(os.listdir())
os.rmdir("my_second_directory")
print(os.listdir())

#remove multipl directories
os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())

#As with the rmdir function, if one of the directories doesn't exist or isn't empty, an exception will be raised.

#The system() function
#All functions presented above can be replaced by a function called system
#which executes a command passed to it as a string.
returned_value = os.system("mkdir my_third_directory")
print(returned_value)


import os

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # Doesn't process a file that isn't a directory.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "/" + dir)
            self.find(current_dir + "/" + entry, dir)


directory_searchv3er = DirectorySearcher()
directory_searchv3er.find("./tree", "python")