import requests, json, lcddriver, time
display = lcddriver.lcd()

api_key = "f5b85d21c52a1b3e17864da8baeba75e"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter City Name: ")
#city_name = "Boise"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

        y = x["main"]

        #(kelvin - 273.15) * (9/5) + 32
        current_temperature = ((y["temp"] - 273.15) * (9/5) + 32)
        current_temp_max = ((y["temp_max"] - 273.15) * (9/5) + 32)
        current_temp_min = ((y["temp_min"] - 275.15) * (9/5) + 32)

        current_temperature = round(current_temperature)
        current_temp_max = round(current_temp_max)
        current_temp_min = round(current_temp_min)

        city_id = x["name"]

        z = x["weather"]
        weather_description = z[0]["description"]

        print("Description: " + str(weather_description))
        print("Temp: " + str(current_temperature))
        print("High: " + str(current_temp_max))
        print("Low: " + str(current_temp_min))


        try:
                while True:
                        display.lcd_display_string(str(city_id) ,1)
                        display.lcd_display_string("Temp: " + str(current_temperatu$                        time.sleep(5)
                        display.lcd_clear()

                        display.lcd_display_string("High: " + str(current_temp_max)$                        display.lcd_display_string("Low: " + str(current_temp_min) $                        time.sleep(5)
                        display.lcd_clear()

                        response = requests.get(complete_url)
        except KeyboardInterrupt:
                display.lcd_clear()

else:
	print("City Not Found ")
