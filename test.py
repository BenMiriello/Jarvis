import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
    print('say something...')
    r.pause_threshold = 0.5
    # r.adjust_for_ambient_noise(source)
    r.energy_threshold = 2000
    audio = r.listen(source)
try:
    recog = r.recognize_google(audio, language = 'en-US')

    print('you said: ' + recog)
except sr.UnknownValueError:
    print('Google speech recognition could not understand audio')
except sr.RequestError as e:
    print('Could not request results from google speech recognition service: {0}'.format(e))
