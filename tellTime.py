import datetime
from speak import speak

def conditions(query):
  return "what time is it" in query

def response(query=None):
  time = str(datetime.datetime.now())

  print(time)
  hour = time[11:13]
  min = time[14:16]
  speak("The time is " + hour + "Hours and" + min + "Minutes")
