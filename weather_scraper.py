# import openmeteo_requests

# import requests_cache
# import pandas as pd
# from retry_requests import retry

# # Setup the Open-Meteo API client with cache and retry on error
# cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
# retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
# openmeteo = openmeteo_requests.Client(session = retry_session)

# # Make sure all required weather variables are listed here
# # The order of variables in hourly or daily is important to assign them correctly below
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
# 	"latitude": 12.9719,
# 	"longitude": 77.5937,
# 	"current": ["temperature_2m", "is_day"],
# 	"hourly": "temperature_2m",
# 	"timezone": "auto",
# 	"forecast_days": 1
# }
# responses = openmeteo.weather_api(url, params=params)

# # Process first location. Add a for-loop for multiple locations or weather models
# response = responses[0]
# print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
# print(f"Elevation {response.Elevation()} m asl")
# print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
# print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# # Process hourly data. The order of variables needs to be the same as requested.
# hourly = response.Hourly()
# hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

# hourly_data = {"date": pd.date_range(
# 	start = pd.to_datetime(hourly.Time(), unit = "s"),
# 	end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
# 	freq = pd.Timedelta(seconds = hourly.Interval()),
# 	inclusive = "left"
# )}
# hourly_data["temperature_2m"] = hourly_temperature_2m

# hourly_dataframe = pd.DataFrame(data = hourly_data)
# print(hourly_dataframe)


# --------------------------------------------------------------------------------------------------- #

# API_key = "c9d4c0f1fb50e0f4786f71ad1446fdc9"
lon = 77.625
lat = 13.0

# import required modules
import requests, json
 
# Enter your API key here
api_key = "bb23e28c90cb84bb52a8071af9ba1a99"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
city_name = input("Enter city name : ")
 
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object 
# convert json format data into
# python format data
x = response.json()
print(x)
 
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
# if x["cod"] != "404":
 
#     # store the value of "main"
#     # key in variable y
#     y = x["main"]
 
#     # store the value corresponding
#     # to the "temp" key of y
#     current_temperature = y["temp"]
 
#     # store the value corresponding
#     # to the "pressure" key of y
#     current_pressure = y["pressure"]
 
#     # store the value corresponding
#     # to the "humidity" key of y
#     current_humidity = y["humidity"]
 
#     # store the value of "weather"
#     # key in variable z
#     z = x["weather"]
 
#     # store the value corresponding 
#     # to the "description" key at 
#     # the 0th index of z
#     weather_description = z[0]["description"]
 
#     # print following values
#     print(" Temperature (in kelvin unit) = " +
#                     str(current_temperature) +
#           "\n atmospheric pressure (in hPa unit) = " +
#                     str(current_pressure) +
#           "\n humidity (in percentage) = " +
#                     str(current_humidity) +
#           "\n description = " +
#                     str(weather_description))
 
# else:
#     print(" City Not Found ")