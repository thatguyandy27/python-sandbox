#
# Example file for working with Calendars
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


import calendar

c = calendar.TextCalendar(calendar.SUNDAY)

str = c.formatmonth(2013, 1, 0, 0)

print(str)
