import os 
from dotenv import load_dotenv

load_dotenv()
course_key = os.getenv("COURSE_API")
wind_key = os.getenv("WINDY_API")