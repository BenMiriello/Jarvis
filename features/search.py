import webbrowser

from utilities.speak import speak

def conditions(query):
  validQueries = [
    'open google'
  ]

  return any(string in query for string in validQueries)


def response(query=None):
  speak("Opening Google ")
  webbrowser.open('www.google.com')