from utilities.takeCommand import takeCommand
from utilities.respond import respond
from features.index import runPrimaryConditions
from features.hello import hello
import features.goodbye

def takeQuery():
  hello()
  while(True):
    query = takeCommand()

    conditionsMet = not runPrimaryConditions(query)

    if conditionsMet and goodbye.conditions(query):
      respond(query, goodbye)
      exit()

if __name__ == '__main__':
  takeQuery()