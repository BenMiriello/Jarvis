# import time
# import os
# import subprocess
# from ecapture import ecapture as ec
# import wolframalpha
# import json
# import requests

from speak import speak
from takeCommand import takeCommand
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
      search.response()
      continue

    elif tellDay.conditions(query):
      tellDay.response()
      continue

    elif tellTime.conditions(query):
      tellTime.response()
      continue

    elif searchWikipedia.conditions(query):
      searchWikipedia.response(query)
      continue

    elif goodbye.conditions(query):
      goodbye.response()
      exit()

if __name__ == '__main__':
  Take_query()