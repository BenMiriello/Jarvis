from utilities.takeCommand import takeCommand
from utilities.respond import respond
from features.index import runConditions
from features.hello import hello
from features import goodbye

def takeQuery():
  hello()
  while(True):
    query = takeCommand()
    print(query)

    conditionsMet = runConditions(query)

    if not conditionsMet and goodbye.conditions(query):
      respond(query, goodbye)
      exit()

if __name__ == '__main__':
  takeQuery()