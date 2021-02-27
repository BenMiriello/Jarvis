import speech_recognition as sr
from record_to_file import record_audio

r = sr.Recognizer()
r.energy_threshold = 500
# mic = sr.Microphone(device_index = 1)

def record_and_interpret():
    print('speak now')
    while True:
        with sr.Microphone() as source:
            # audio = r.record(source)
            audio = r.listen(source)
            spoken = r.recognize_google(audio)
            print('you said ' + spoken)

if __name__ == '__main__':
    record_and_interpret()
