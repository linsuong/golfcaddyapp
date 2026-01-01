import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()

course_key = os.getenv("COURSE_API")
wind_key = os.getenv("WINDY_API")

course_url = "https://api.golfcourseapi.com"
    
def course_healthcheck():
    
    url = f"{course_url}/v1/healthcheck"
    
    try:
        response = requests.get(url)
        print(f"healthcheck: {response.status_code}")
        #print(response.text)
        
        if response.status_code == 200:
            print("course health check good")
            
        return response.status_code == 200
    
    except Exception as e:
        print(f"healthcheck failed: {e}")
        
        return False


def search_course(search_term):
    while True:
        url = f"{course_url}/v1/search"
        
        headers = {"Authorization": f"Key {course_key}"}
        
        params = {"search_query": search_term}

        print(f"searching for closest match to: {search_term}")

        try:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 401:
                print("error: UnauthorizedError")
                return None

            if response.status_code != 200:
                print(f"error {response.status_code}: {response.text}")
                continue

            data = response.json()
            courses = data.get("courses", [])

            print(f"found {len(courses)} courses")

            if len(courses) == 0:
                print("No courses found. Please try again.\n")
                continue 

            # Save only if results exist
            with open("data/search_results.json", "w") as f:
                json.dump(data, f, indent=2)

            print("saved to: data/search_results.json")
            return data

        except Exception as e:
            print(f"Search failed: {e}")

if __name__ == "__main__":
    print(course_key)
    
    course_healthcheck()

    search_course('Scotland')