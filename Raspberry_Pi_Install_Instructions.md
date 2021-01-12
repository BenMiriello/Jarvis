# Raspbery Pi Installation Instructions
Not complete yet

## Setting up the local environment and python packages

Clone repo
```git clone https://github.com/BenMiriello/Jarvis.git```

Navigate into directory
```cd Jarvis```

Install pip3
```sudo apt install pip3```

Install venv
```pip3 install virtualenv```

Create virtual environment
```python3 -m venv .venv```

Activate virtual environment
```source .venv/bin/activate```

Install dependencies from requirements.txt
```pip3 install -r requirements.txt```

If you receive an error that reads 'Could not find a version that satisfies the requirement...', there are many suggested fixes you can find and try on the internet. Feel free to try some of them. I found it was faster to try running `python3 index.py` and installing whatever turned up as a 'ModuleNotFoundError'.
```pip3 install speechRecognition```

You will probably need to install espeak on your system
```sudo apt-get update && sudo apt-get install espeak```

Most packages can be installed with this one command
```pip3 install speechRecognition playsound pyttsx3 speake3 word2number wikipedia```

For package gi, follow the directions here [https://pygobject.readthedocs.io/en/latest/getting_started.html#ubuntu-getting-started](https://pygobject.readthedocs.io/en/latest/getting_started.html#ubuntu-getting-started).

I had issues with package 'gi' not having python3-friendly syntax, giving me the error "SyntaxError: Missing parentheses in call to 'print'. Did you mean print(url)?" If you're using python3, you may also need to convert that package using 2to3.

Install 2to3
```pip3 install 2to3```

Then run the conversion.
```2to3 -w .venv/lib/python3.7/site-packages/gi/__init__.py```

If you see "AttributeError: module 'gi' has no attribute 'require_version'.", you may need to refer again to the instructions above. I had accidentally installed another package called 'gi' using pip3 which was being imported intead of the right import. I had to make sure the wrong one was uninstalled. For me, that meant starting over with a new cloned repo, but you may be able to not make my initial mistake or just uninstall it and use the right one. 
<!-- attempted and failed methods: -->
<!-- install gobject. -->
<!-- ```sudo apt-get install python-gobject```-->
<!-- ```sudo apt install python-gi python-gi-cairo python3-gi python3-gi-cairo gir1.2-gtk-3.0``` -->
<!-- ```sudo apt install python3-gst-1.0``` -->
<!-- ```sudo apt-get install python3-gi``` -->
<!-- sudo apt-get install libgirepository1.0-dev
python -m pip install --user pygobject -->

After seeing Could not find PyAudio: ```pip3 install PyAudio``` and ```sudo apt-get install libportaudio-dev```

This got me to the stage of being able to run the program, however you'll still need to connect to mic in in order to take commands and talk back.

## Connecting to microphone and speaker

At this stage I started connecting to my raspberry pi via ssh over local wifi rather than by connecting a monitor, keyboard, and mouse directly to the pi. Because I didn't have a compatable usb hub at the time, this freed up the usb connection for my usb mic/speaker. You'll have to setup your pi to run in a headless state (without being connected to keyboard and monitor) eventually, so while you could wait now isn't a bad time to do so. I found these instructions were the most helpful for this process: [https://desertbot.io/blog/headless-raspberry-pi-3-bplus-ssh-wifi-setup](https://desertbot.io/blog/headless-raspberry-pi-3-bplus-ssh-wifi-setup).

To configure audio, I used this resource: [https://pimylifeup.com/raspberrypi-microphone/](https://pimylifeup.com/raspberrypi-microphone/).
<!-- [https://iotbytes.wordpress.com/connect-configure-and-test-usb-microphone-and-speaker-with-raspberry-pi/](https://iotbytes.wordpress.com/connect-configure-and-test-usb-microphone-and-speaker-with-raspberry-pi/).  -->

To configure audio, we can start by checking that our device is connected by running `arecord -l` in your pi terminal. For me it returned the following:
```
card 1: iTalk02 [ iTalk-02], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

What you need from this is the card and device number. For me those are 1 and 0.

Then you'll create or edit a file at `/home/pi/.asoundrc`. If you're in `/home/pi`, you'll run `vim .asoundrc`.
If you're not familiar with vim, you just need to know to hit `i` first to enter 'insert' mode, then type the instructions below as though in a regular code editor. Then to leave press 'esc' then type `:wq` to save the file and exit vim (or `:q` to just exit).

In this file you'll want to add these lines:
```
pcm.!default{
  type asym
  capture.pcm "mic"
}
pcm.mic {
  type plug
  slave {
    pcm "hw:1,0"
  }
}
```
Note that after "hw:" you'll put your own card and device numbers you got from 'arecord -l' in the last step.

To test the mic, run `arecord --format=S16_LE --rate=16000 --file-type=wav out.wav` to record to a file called 'out.wav'. Then hit `cmd + c` to stop recording and `aplay out.wave` to play back.

<!-- Need to connect a speaker to play back next! -->

<!-- ```
Bus 001 Device 002: ID 0909:005f Audio-Technica Corp. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
``` -->

<!-- [NEW] Device 08:EB:ED:44:63:E1 Soundcore Flare Mini -->

https://pimylifeup.com/raspberrypi-microphone/
