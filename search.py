import webbrowser

def conditions(query):
  return "open google" in query

def response():
      speak("Opening Google ")
      webbrowser.open('www.google.com')