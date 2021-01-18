import time
import sys
from word2number import w2n

from utilities.speak import speak

def conditions(query):
  validQueries = [
    'set a timer',
    'set timer',
    'timer',
  ]

  return any(string in query for string in validQueries) if query else None

def plural(integer):
  return 's' if integer > 1 else ''

def response(query):
  query_array = query.split()

  def query_time(increment):
    index = 1
    if increment in query_array:
      index = query_array.index(increment)
    elif increment + 's' in query_array:
      index = query_array.index(increment + 's')
    else:
      return 0

    try:
      return w2n.word_to_num(query_array[index - 1])
    except:
      return 0

  seconds = query_time('second')
  minutes = query_time('minute')
  hours = query_time('hour')

  seconds_now = minutes_now = hours_now = 0

  time_start = time.time()

  initial_report = "\n\rSetting timer for {hours}{minutes}{seconds}".format(
    hours = str(hours) + ' hours ' if (hours > 0) else '',
    minutes = str(minutes) + ' minutes ' if (minutes > 0) else '',
    seconds = str(seconds) + ' seconds ' if (seconds > 0) else ''
  )
  print(initial_report)
  speak(initial_report)

  while True:
    try:
      print("\r{hours}{minutes}{seconds}".format(
        hours = str(hours_now) + ' hour' + plural(hours_now) + ' ' if (hours_now > 0) else '',
        minutes = str(minutes_now) + ' minute' + plural(minutes_now) + ' ' if (minutes_now > 0) else '',
        seconds = str(seconds_now) + ' second' + plural(seconds_now) + ' ' if (seconds_now > 0) else ''
      ))

      time.sleep(1)
      seconds_now = int(time.time() - time_start) - minutes_now * 60

      if seconds_now >= 60:
        minutes_now += 1
        seconds_now = 0

      if minutes_now >= 60:
        hours_now += 1
        minutes_now = 0
        seconds_now = 0

      if hours <= hours_now:
        if minutes <= minutes_now:
          if seconds <= seconds_now:
            final_report = "\n\rTimer is up\n"
            print(final_report, end=' ', flush=True)
            speak(final_report)

            break

    except KeyboardInterrupt as e:
      break
