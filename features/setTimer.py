import time
import sys

from utilities.speak import speak

def conditions(query):
  validQueries = [
    'set a timer',
    'set timer',
    'timer',
  ]

  return any(string in query for string in validQueries)

def response(query=None):
  time_start = time.time()

  end_hours = 0
  end_minutes = 0
  end_seconds = 10

  seconds = 0
  minutes = 0
  hours = 0

  initial_report = "\n\rSetting timer for {hours}{minutes}{seconds}".format(
    hours = str(end_hours) + ' hours ' if (end_hours > 0) else '',
    minutes = str(end_minutes) + ' minutes ' if (end_minutes > 0) else '',
    seconds = str(end_seconds) + ' seconds ' if (end_seconds > 0) else ''
  )
  print(initial_report)
  speak(initial_report)

  while True:
    try:
      print("\r{hours}{minutes}{seconds}".format(
        hours = str(hours) + ' hours ' if (hours > 0) else '',
        minutes = str(minutes) + ' minutes ' if (minutes > 0) else '',
        seconds = str(seconds) + ' seconds ' if (seconds > 0) else ''
      ))

      time.sleep(1)
      seconds = int(time.time() - time_start) - minutes * 60

      if seconds >= 60:
        minutes += 1
        seconds = 0

      if minutes >= 60:
        hours += 1
        minutes = 0
        seconds = 0

      if end_hours <= hours:
        if end_minutes <= minutes:
          if end_seconds <= seconds:
            final_report = "\n\rTimer is up\n"
            print(final_report, end=' ', flush=True)
            speak(final_report)

            break

    except KeyboardInterrupt as e:
      break
