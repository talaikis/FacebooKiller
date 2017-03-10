# FacebooKiller

I had created this tool after noticing how much time I waste on Facebook. FB is great time killer and I don't like that, so thoght, why not to kill Facebook (and any other sites) instead? This simple app will alert with sound One after aprox. 30 seconds on Facebbok, then minimize window after 50 with sound no. Two and finally, after 120s will shut down the browser.

## Inputs

```text
# alert after this time
time_limit_stage_one = 30

# minimize the window after this time
time_limit_stage_two = 50

# killl chrome if nothing helps
time_limit_stage_three = 120
```

## Use without build

* Obviously you need Python (3.6).
* Install requiremrnts ```pip install -r requirements.txt```
* Edit the killer.py inputs.
* Move killer/ folder to your user path, e.g.: C:\Users\[username]\killer
* Move fb-killer-starter.bat to C:\Users\[username]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

Voila, FacebooKiller will start with the machine boot.

## How to build

```text
pyinstaller --onefile killer.py
```

Then you'll find your killer.exe in dist/

## Prerequisites

Works on Windows (8.1 tested) with Google Chrome.

## Known issues

* .exe doesn't play audio files (Python 3.6, Pyintslaler dev.)
