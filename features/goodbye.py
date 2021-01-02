from utilities.speak import speak

def conditions(query):
  return 'bye' in query

def response(query=None):
  speak("See you later alligator.")