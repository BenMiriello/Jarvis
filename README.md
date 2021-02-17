# Digital Assistant

Designed to run on a Raspberry Pi, but works on any system with a cli, python, and a mic and speaker.

Run with command ```python3 index.py ```

## Preliminary Features

- Tell Time

- Tell Day

- Set a Timer

## Upcoming Features

Listed [here](TODO.md)

## Running on Raspberry Pi

Refer to [Raspberry Pi Installation Instructions](Raspberry_Pi_Install_Instructions.md) to get started.

<!--
## Settings
In [utilities/takeCommand.py](utilities/takeCommand.py), on  the `with sr.Microphone...` line, you may need to pass an argument of the device_index like this:  
```with sr.Microphone(device_index=0) as source:```  
Or you may not want to set a microphone at all and let the system choose it for you. This may be the case on a mac, where the system will usually pick a working audio out port for you, though it may not be the one you want. For configuring a Raspberry Pi, however, you will likely have to set a mic_port for speech recognition. Check which port you want to use like this:
```
$ python3
>>> import speech_recognition as sr
>>> sr.Microphone.list_microphone_names()
```
The index of the mic you want in the array should be the mic_port.
-->
