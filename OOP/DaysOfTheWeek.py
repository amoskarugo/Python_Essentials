class WeekDayError(Exception):
    pass
	

class Weeker:
    days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
    def __init__(self, day):
        try:
            self.week_day = day
            p = self.days.index(self.week_day.lower())
        except ValueError:
            raise WeekDayError
        # Write code here.
        #

    def __str__(self):
        return self.week_day

    def add_days(self, n):
        pos = 0
        for i in self.days:
            if self.week_day.lower() == i.lower():
                pos = self.days.index(i)
        current = pos
        length = pos + n
        while  length:
            if current > 6:
                current = 0
            current += 1
            length -= 1
        self.week_day = self.days[current]
            
        

        # Write code here.
        #

    def subtract_days(self, n):
        pos = 0
        for i in self.days:
            if self.week_day.lower() == i.lower():
                pos = self.days.index(i)
        current = pos
        length = pos + n
        while length:
            current -= 1
            if current < 0:
                current = 6
            length -= 1


        self.week_day = self.days[current]
        #


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(2)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")