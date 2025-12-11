import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()

course_key = os.getenv("COURSE_API")
wind_key = os.getenv("WINDY_API")

print(course_key)

course_url = "https://api.golfcourseapi.com"
    
def course_healthcheck():
    
    url = f"{course_url}/v1/healthcheck"
    
    try:
        response = requests.get(course_url)
        print(f"healthcheck: {response.status_code}")
        print(response.text)
        
        if response.status_code == 200:
            print("course health check good")
            
        return response.status_code == 200
    
    except Exception as e:
        print(f"healthcheck failed: {e}")
        
        return False


def search_course(search_term):
    
    url = f"{course_url}/v1/search"
    
    headers = {
        "auth": course_key
    }
    
    params = {
        "search_query": search_term
    }
    
    print(f"searching for closest match to: {search_term}")
    
    try:
        response = requests.get(course_url)
        print(f"healthcheck: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"found {len(data.get('courses', []))} courses")
            
            
    except Exception as e:
        print(f"Search failed: {e}")
        return None
    
def main():
    print("=== Testing Golf Course API ===\n")

    # Step 1: Test healthcheck
    print("1. Testing API healthcheck...")
    if not course_healthcheck():
        return

    # Step 2: Search for a course
    print("\n2. Searching for a course...")
    search_term = input("enter course name (default = pinehurst)").strip()
    if not search_term:
        search_term = "pinehurst"

    search_result = search_course(search_term)
        
if __name__ == "__main__":
    main()