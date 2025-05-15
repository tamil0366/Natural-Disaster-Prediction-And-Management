rainfall = float(input("Enter rainfall (mm): "))
wind_speed = float(input("Enter wind speed (km/h): "))
humidity = float(input("Enter humidity (%): "))
temperature = float(input("Enter temperature (°C): "))

if rainfall > 250 and wind_speed > 70 and humidity > 85:
    print("ALERT: High risk of natural disaster! Take immediate precautions.")
else:
    print("No disaster predicted.Conditions are normal.")