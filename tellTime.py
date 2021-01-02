import datetime
from speak import speak

def conditions(query):
  return "what time is it" in query

def response(query=None):
  time = str(datetime.datetime.now())

  print(time)
  hours = str(int(time[11:13]) % 12)
  minutes = time[14:16].lstrip('0')
  
  speak("The time is " + hours + ' ' + minutes)