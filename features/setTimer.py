import time
import sys

# def conditions(query):
#   return False

# def response(query):
#   return True



# TEST 1 #########################################################

# class TimerError(Exception):
#   'Timer Error'

# class Timer:
#   def __init__(self):
#     self._start_time = None

#   def start(self):
#     'Starting a new timer'
#     if self._start_time is not None:
#       raise TimerError(f'Timer is running. Use .stop() to stop')

#     self._start_time = time.perf_counter()

#   def stop(self):
#     'Stop the timer and report elapsed time'
#     if self._start_time is None:
#       raise TimerError(f'Timer is not running. Use .start() to start')

#     elapsed_time = time.perf_counter() - self._start_time
#     self._start_time = None
#     print(f'Elapsed time: {elapsed_time:0.4f} seconds')

# if __name__ == '__main__':
#   main()


# TEST 2 #########################################################

time_start = time.time()
seconds = 0
minutes = 0

while True:
  try:
    print("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
    time.sleep(1)
    seconds = int(time.time() - time_start) - minutes * 60
    if seconds >= 60:
      minutes += 1
      seconds = 0
  except KeyboardInterrupt as e:
    break