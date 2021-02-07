import speech_recognition as sr
from record_to_file import record_audio

r = sr.Recognizer()
# mic = sr.Microphone(device_index = 1)

def record_and_interpret():
    print('speak now')
    record_audio(5)
    just_recorded = sr.AudioFile('spoken.wav')
    with just_recorded as source:
        audio = r.record(source)
        spoken = r.recognize_google(audio)
        print('you said ' + spoken)

if __name__ == '__main__':
    record_and_interpret()
