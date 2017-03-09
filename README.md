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

## Installation & how to use

...

Fast workaround. Change killer.py to killer.pyw and open with pytonw, it will run in background.

## How to build

```text
pyinstaller --onefile killer.py
```

Then you'll find your killer.exe in dist/

## Prerequisites

Works on Windows with Google Chrome only.

# Known issues

* .exe doesn't play audio files (Python 3.6, Pyintslaler dev.)
