#
# Example file for working with timedelta objects
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

print("One year from now will be " + str(datetime.now() + timedelta(days=365)))

print("In two days and three weeks it will be " + str(datetime.now() + timedelta(weeks=3, days=2)))
