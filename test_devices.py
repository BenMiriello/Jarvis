import pyaudio, audioop

CHANNELS = 2
RATE = 44100
CHUNK = 4096
FORMAT = pyaudio.paInt16

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
sample_size = pyaudio.get_sample_size(FORMAT)
try:
  while True:
    buffer = stream.read(CHUNK)
    left_frames, right_frames = audioop.tomono(buffer, sample_size, 1, 0), audioop.tomono(buffer, sample_size, 0, 1)
except KeyboardInterrupt: pass
stream.stop_stream()
stream.close()
p.terminate()