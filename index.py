from takeCommand import takeCommand
from respond import respond
from hello import hello
import goodbye
import tellTime
import tellDay
import search
import searchWikipedia

def Take_query():
  hello()
  while(True):
    query = takeCommand()

    if search.conditions(query):
      respond(query, search)
      continue

    elif tellDay.conditions(query):
      respond(query, tellDay)
      continue

    elif tellTime.conditions(query):
      respond(query, tellTime)
      continue

    elif searchWikipedia.conditions(query):
      respond(query, searchWikipedia)
      continue

    elif goodbye.conditions(query):
      respond(query, goodbye)
      exit()

if __name__ == '__main__':
  Take_query()