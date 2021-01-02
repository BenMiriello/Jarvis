from takeCommand import takeCommand
from respond import respond
from runPrimaryConditions import runPrimaryConditions
from hello import hello
import goodbye

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