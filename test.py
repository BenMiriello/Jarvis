import speech_recognition as sr

r = sr.Recognizer()
speech = sr.Microphone(device_index=1)

with speech as source:
    print('say something...')
    audio = r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    recog = r.recognize_google(audio, language = 'en-US')

    print('you said: ' + recog)
except sr.UnknownValueError:
    print('Google speech recognition could not understand audio')
except sr.RequestError as e:
    print('Could not request results from google speech recognition service: {0}'.format(e))
