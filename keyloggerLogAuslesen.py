#Daten werden aus dem JSON File log.txt ausgelesen es werden nur die Down-Strokes ausgelesen hier wir dann der Name angegeben (Taste)
import json

with open("./log.txt", "r") as file:
	for line in file:
		data = json.loads(line)
		if data["event_type"] == "down":
			print(data["name"])
			
			
