
def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s

class Timer:
    def __init__(self, h = 0, m = 0, s = 0):
        self.__hour = h
        self.__min = m
        self.__sec = s
    
    def __str__(self):
        return two_digits(self.__hour) + ":" + two_digits(self.__min) + ":" + two_digits(self.__sec)
    

    def next_second(self):
        self.__sec = self.__sec + 1
        if self.__sec > 59:
            self.__sec = self.__sec - 60
            self.__min +=1
            if self.__min > 59:
                self.__min -= 60
                self.__hour += 1
                if self.__hour > 23:
                    self.__hour -= 24
        else:
            self.__sec = self.__sec + 1

    def prev_second(self):
        time = self.__str__().split(":")
        if int(time[2]) < 1:
            self.__sec = 60 - 1
            self.__hour = 24 - 1
            self.__min = 60 -1
        # Write code here
        #

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)