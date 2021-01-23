# Digital Assistant

## Preliminary Features

- Tell Time

- Tell Day

- Set a Timer

## Running on Raspberry Pi

Refer to [Raspberry Pi Installation Instructions](Raspberry_Pi_Install_Instructions.md) in the root directory to get started.

## Settings
You can create a file called `settings.py` in the root directory based on `settings_example.py`.

On a mac, you may not need to set an audio port. The system will usually pick a working audio out port for you. However, it may not be the one you want. For configuring a Raspberry Pi, however, you will have to set a mic_port in settings for speech recognition. Check which port you want to use like this:
```
$ python3
>>> import speech_recognition as sr
>>> sr.Microphone.list_microphone_names()
```
The index of the mic you want in the array should be the mic_port.
