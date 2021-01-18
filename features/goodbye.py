from utilities.speak import speak

def conditions(query):
  return 'bye' in query if query else None

def response(query=None):
  speak("See you later alligator.")