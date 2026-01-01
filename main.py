from api import course_api 
from api.windy_api import wind_forecast
from data import data_process

search_term = input("Welcome! Please enter search for golf course: ")

course_api.search_course(search_term)

wind_data = data_process.load_json("data/wind_data.json")
course_data = data_process.load_json("data/search_results.json")

choice = data_process.select_course(course_data)

print(type(choice))
print(f"Your choice is: {choice["course_name"]} at {choice["location"]["city"]}, {choice["location"]["country"]}.")

wind_forecast(choice["location"]["latitude"], choice["location"]["longitude"])

surface_temp = wind_data["temp-surface"][0] - 273.15
speed_mph, direction = data_process.get_current_wind(wind_data)

print(f"Current wind speed is: {speed_mph:.2f} mph @ {direction:.3f} degrees")
print(f"Surface Temp is: {surface_temp}")
