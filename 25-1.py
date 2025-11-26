class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__normalize()

    # Private normalize method
    def __normalize(self):
        if self.__seconds >= 60:
            self.__minutes += self.__seconds // 60
            self.__seconds %= 60

        if self.__minutes >= 60:
            self.__hours += self.__minutes // 60
            self.__minutes %= 60

        if self.__hours >= 24:
            self.__hours %= 24

    # Overloading-style method without *args
    def add_time(self, other=None, hours=0, minutes=0, seconds=0):

        # Case 1: Time object passed
        if isinstance(other, Time):
            self.__hours += other.__hours
            self.__minutes += other.__minutes
            self.__seconds += other.__seconds

        # If someone passed a wrong type
        elif other is not None:
            print("Invalid argument. Pass a Time object OR use hours/minutes/seconds.")
            return

        # Case 2: Numeric values passed
        else:
            self.__hours += hours
            self.__minutes += minutes
            self.__seconds += seconds

        self.__normalize()

    # Display Time
    def display(self):
        print(f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}")


t1 = Time(2, 45, 50)
t2 = Time(1, 30, 20)

print("Initial times:")
t1.display()
t2.display()

print("\nAdding Time object:")
t1.add_time(t2)
t1.display()

print("\nAdding hours, minutes & seconds:")
t1.add_time(hours=2, minutes=40, seconds=50)
t1.display()
