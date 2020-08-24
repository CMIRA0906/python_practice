import json

weather=json.loads('{ 		"temp": 288.3, 		"feels_like": 284.68, 		"temp_min": 287.04, 		"temp_max": 289.82, 		"pressure": 1014, 		"humidity": 77 	}')
#Mostrar claves del diccionario
for x in weather:
    print(x)