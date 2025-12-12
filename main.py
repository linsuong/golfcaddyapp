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
        "Authorization": f"Key {course_key}"
    }
    
    params = {
        "search_query": search_term
    }
    
    print(f"searching for closest match to: {search_term}")
    
    try:
        response = requests.get(url, headers=headers, params=params)
        # print(f"search response: {response.status_code}")
        
        if response.status_code == 401:
            print("error: UnauthorizedError")
            
        if response.status_code == 200:
            data = response.json()
            print(f"found {len(data.get('courses', []))} courses")

            with open('data/search_results.json', 'w') as f:
                json.dump(data, f, indent = 2)
                
            print("saved to: data/search_results.json")
            
            return data
        
        else: 
            print(f'error, {response.status_code}, {response.text}')
            
    except Exception as e:
        print(f"Search failed: {e}")
        return None


def wind_forecast(lat, lon):
    url = 'https://api.windy.com/api/point-forecast/v2'
    
    params = {
        "lat": lat,
        "lon": lon,
        "model": 'gfs',
        "parameters": ["temp", "dewpoint", "precip", "wind"],
        "levels": ['surface'],
        "key": wind_key
        }   
    
    headers = {
        "Content-Type": "application/json"
            }
      
    try:
        response = requests.post(url, json=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("wind data obtained for course")
            
            with open('data/wind_data.json', 'w') as f:
                json.dump(data, f, indent = 2)
                
            print("saved to: data/wind_data.json")
            
            return data
        
        else: 
            print(f'error, {response.status_code}, {response.text}')
            
    except Exception as e:
        print(f"Search failed: {e}")
        return None
