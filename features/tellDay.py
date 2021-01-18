import datetime
from utilities.speak import speak

def conditions(query):
  validQueries = [
    'what day is it',
    'what day is',
    'day is it',
    'what day',

    'what day is today',
    'what is today',
    'is today',
    'what day is',

    'tell me the day',
    'tell day',
    'me what day',

    'what is the day',
    'is the day',

    'todays date',
    "today's date",

    "what's the day",
    'whats the day',

    'when are we',
  ]

  return any(string in query for string in validQueries) if query else None

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