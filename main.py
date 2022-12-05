from pywttr import Wttr

city=input("Enter Your City: ")
wttr = Wttr(city)
forecast = wttr.en()
temp = forecast.weather[0].avgtemp_c

print("Today's average temperature in ", city, " is ", temp, "°C")
