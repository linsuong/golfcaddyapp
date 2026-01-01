import json 
import math 

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def wind_speed_and_dir(u, v):
    speed = math.sqrt(u**2 + v**2)  # m/s
    direction = (math.degrees(math.atan2(u, v)) + 360) % 360
    return speed, direction

def ms_to_mph(ms):
    return ms * 2.23694

def get_current_wind(wind_data):
    u = wind_data["wind_u-surface"][0]
    v = wind_data["wind_v-surface"][0]

    speed, direction = wind_speed_and_dir(u, v)
    return ms_to_mph(speed), direction

def select_course(course_data):
    courses = course_data["courses"]

    print("\nAvailable courses:")
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course['course_name']}")

    while True:
        choice = input("\nSelect a course number: ")
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(courses):
                return courses[idx]

        print("Invalid selection. Please try again.")
        
        return choice


if __name__ == "__main__":
    wind_data = load_json("data/wind_data.json")
    course_data = load_json("data/search_results.json")

    surface_temp = wind_data["temp-surface"][0] - 273.15
    
    choice = select_course(course_data)
    #print(choice)
    
    course_name = choice["course_name"]
    print(choice["club_name"])
    speed_mph, direction = get_current_wind(wind_data)
    
    print(f"Current wind speed on {course_name} is: {speed_mph} mph @ {direction}")
    print(f"Surface Temp is: {surface_temp}")
    
    print(choice['tees']['male'][0]['holes'][0])

