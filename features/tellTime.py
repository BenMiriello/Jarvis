import datetime
from utilities.speak import speak

def conditions(query):
  validQueries = [
    'what time is it',
    'what time is',
    'time is it',
    'tell me the time',
    'tell time',
    'how early is it',
    'how late is it',
    'what is the time',
    'is the time',
    "what's the time",
    'whats the time',
  ]

  return any(string in query for string in validQueries) if query else None

def response(query=None):
  time = str(datetime.datetime.now())

  print(time)
  hours = str(int(time[11:13]) % 12)
  minutes = time[14:16].lstrip('0')

  speak("The time is " + hours + ' ' + minutes)