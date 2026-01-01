import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()

wind_key = os.getenv("WINDY_API")

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
    
    
if __name__ == "__main__":
    wind_forecast(50, 50)
