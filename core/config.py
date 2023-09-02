import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    
    # Load the environment variables from the .env file
    load_dotenv()
    
    APP_NAME: str = "My App"
    APP_VERSION: str = "0.0.1"
    DEBUG: bool = os.getenv("DEBUG", False)
    
    
def get_settings():
       return Settings()