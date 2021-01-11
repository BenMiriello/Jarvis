# Raspbery Pi Installation Instructions
Not complete yet

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

If you see "AttributeError: module 'gi' has no attribute 'require_version'.", ...TBD. <!-- install gobject. -->
<!-- ```sudo apt-get install python-gobject```-->
<!-- ```sudo apt install python-gi python-gi-cairo python3-gi python3-gi-cairo gir1.2-gtk-3.0``` -->
<!-- ```sudo apt install python3-gst-1.0``` -->
<!-- ```sudo apt-get install python3-gi``` -->
<!-- sudo apt-get install libgirepository1.0-dev
python -m pip install --user pygobject -->
