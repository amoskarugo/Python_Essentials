import time
from datetime import date, time, datetime

#Getting the current local date and creating date objects
#one of the classes provided by the datetime module is a class class called date.
#objects of this class represent a date consisting of the year, month and day

today = date.today()

print(today)
print("year", today.year)
print("month", today.month)
print("day", today.day)

#creating a date object

my_date = date(2019, 12, 4)
print(my_date)

#creating a date object from a timestamp
#date class gives us the ability to create a date object from a timestamp
#the timestamp expresses the number of seconds since january 1, 1970, 00:00:00(UTC), expreesed in seconds
#to create a date object from  a timestamp, you must pass a unix timestamp to the fromtimestamp method
#use time module that provides time-related function
#function time() returns the number of seconds from january 1, 1970 to the current moment in the form ofa float number.

timestamp = time.time()
print("timestamp", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

#creating a date object using the ISO  format
#datetime module provides several methods to create a date object. one of them is fromisoformat method
#which takes date in the YYYY-MM-DD format compliant with the ISO 8601 standard

#The replace() method

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

#What day of the week is it?
d = date(2019, 11, 4)
print(d.weekday())#returns an interger 0 is monday 6 is sunday

#alternative day of the week method
d = date(2019, 11, 4)
print(d.isoweekday()) #returns an interger 1 is monday 7 is sunday

#Creating time objects
# t = time(14, 53, 20, 1)
#
# print("Time:", t)
# print("Hour:", t.hour)
# print("Minute:", t.minute)
# print("Second:", t.second)
# print("Microsecond:", t.microsecond)

#4.5.8 The time module

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)

#The ctime() function
timestamp = 1572879180
print(time.ctime(timestamp))
print(time.ctime())# current time will be returned

#Methods that return the current date and time
#The datetime class has several methods that return the current date and time.

"""
These methods are:
- today() — returns the current local date and time with the tzinfo attribute set to None;
- now() — returns the current local date and time the same as the today method, unless we pass the optional argument tz to it.
The argument of this method must be an object of the tzinfo subclass;
- utcnow() — returns the current UTC date and time with the tzinfo attribute set to None.
"""
print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

#Getting a timestamp

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

#Date and time formatting
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

#Date and time operations
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)
