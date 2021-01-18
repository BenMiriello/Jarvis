# Digital Assistant

## Preliminary Features

- Tell Time

- Tell Day

- Set a Timer

## Settings
You can create a file called `settings.py` in the root directory based on `settings_example.py`.

Set mic_port for speech recognition. Check which port you want to use:
```
$ python3
>>> import speech_recognition as sr
>>> sr.Microphone.list_microphone_names()
```
The index of the mic you want in the array should be the mic_port.
