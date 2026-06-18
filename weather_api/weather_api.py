import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("YOUR_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file")



def get_weather(city_name, api_key):
    # Base URL configured for current weather endpoints
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Bundle requirements together to attach cleanly to our web call
    query_parameters = {
        "q": city_name,
        "appid": api_key,
        "units": "metric" # Returns temperature in Celsius rather than Kelvin
    }
    
    try:
        # Request data from the server
        response = requests.get(base_url, params=query_parameters)
        
        # Check if the city was found or if permissions are valid
        if response.status_code == 200:
            # Convert raw text response into accessible Python dictionaries
            weather_data = response.json()
            
            # Parse deep layers of the structured text
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            condition = weather_data["weather"][0]["description"]
            
            # Print localized results to the terminal window
            print(f"\n--- Current Weather in {city_name.title()} ---")
            print(f"Condition: {condition.capitalize()}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
        elif response.status_code == 404:
            print("\nError: The typed city could not be located. Double-check spelling.")
        else:
            print(f"\nError: Server responded with status code {response.status_code}")
            
    except requests.exceptions.RequestException as error:
        print(f"\nFailed to establish connection: {error}")

if __name__ == "__main__":
    user_city = input("Enter a city name: ")
    get_weather(user_city, api_key)
