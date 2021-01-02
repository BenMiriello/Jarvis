from respond import respond

import tellTime
import tellDay
import search
import searchWikipedia

def runPrimaryConditions(query):
  if search.conditions(query):
    respond(query, search)
    return True

  elif tellDay.conditions(query):
    respond(query, tellDay)
    return True

  elif tellTime.conditions(query):
    respond(query, tellTime)
    return True

  elif searchWikipedia.conditions(query):
    respond(query, searchWikipedia)
    return True

  else:
    return False