from utilities.respond import respond

from features import tellTime
from features import tellDay
from features import setTimer
from features import search
from features import searchWikipedia

def runConditions(query):
  if tellDay.conditions(query):
    respond(query, tellDay)
    return True

  elif tellTime.conditions(query):
    respond(query, tellTime)
    return True

  elif setTimer.conditions(query):
    respond(query, setTimer)
    return True

  elif search.conditions(query):
    respond(query, search)
    return True

  elif searchWikipedia.conditions(query):
    respond(query, searchWikipedia)
    return True

  else:
    return False