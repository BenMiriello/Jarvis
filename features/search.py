import webbrowser

from utilities.speak import speak

def conditions(query):
  return "open google" in query

def response(query=None):
  speak("Opening Google ")
  webbrowser.open('www.google.com')