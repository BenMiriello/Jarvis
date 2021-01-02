import datetime
from utilities.speak import speak

def conditions(query):
  return "what day is it" in query

def response(query=None):
  dateAndTime = datetime.datetime.today()

  weekDays = {1: 'Monday',    2: 'Tuesday',
              3: 'Wednesday', 4: 'Thursday',
              5: 'Friday',    6: 'Saturday',
              7: 'Sunday'}

  months = {1: 'January',   2: 'February',
            3: 'March',     4: 'April,',
            5: 'May',       6: 'June',
            7: 'July',      8: 'August',
            9: 'September', 10: 'October',
            11: 'November', 12: 'December'}

  if dateAndTime.weekday() + 1 in weekDays.keys():
    day_of_the_week = weekDays[dateAndTime.weekday() + 1]
    month = months[dateAndTime.month]
    calendar_day = datetime.datetime.today().day
    print(day_of_the_week)
    print(month)
    speak("The day is " + day_of_the_week + ' ' + month + ' ' + str(calendar_day))