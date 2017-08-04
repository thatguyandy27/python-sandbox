#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime


def main():
    today = date.today()
    print("Today's date is ", today)

    print("Date components: ", today.day, today.month, today.year)

    print("Today's weekday # is ", today.weekday())

    now = datetime.now()

    print("Right now is", now)

    time = now.time()

    print("Current time is ", time)

    wd = date.weekday(now)
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "sat", "sunday"]

    print ("Today is which day number %d" % wd)
    print ("Which is a " + days[wd])
  
  
if __name__ == "__main__":
  main();
