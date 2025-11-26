class Time:

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__normalize()

    def __normalize(self):

        if self.__seconds >= 60:
            self.__minutes += self.__seconds//60
            self.__seconds %= 60

        if self.__minutes >= 60:
            self.__hours += self.__minutes//60
            self.__minutes %= 60

        if self.__hours >= 24:
            self.__hours %= 24

    def add_time(self, other=None, hours=0, minutes=0, seconds=0):

        if isinstance(other, Time):
            self.__hours += other.__hours
            self.__minutes += other.__minutes
            self.__seconds += other.__seconds

        elif other is not None:
            print("enter a valid time object or add as values")
        else:
            self.__hours += hours
            self.__minutes += minutes
            self.__seconds += seconds

        self.__normalize()

    def display(self):
        print(f"{self.__hours}:{self.__minutes}:{self.__seconds}")


t1 = Time(1, 30, 26)
t2 = Time(2, 45, 75)


t1.display()
t2.display()

t1.add_time(t2)
t1.display()

t1.add_time(hours=2, minutes=30, seconds=42)
t1.display()
