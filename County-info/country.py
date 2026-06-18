import requests
import os
from dotenv import load_dotenv
from streamlit import json
import json

load_dotenv(override=True)
api_key = os.getenv("YOUR_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file")

def get_status(country_name):
    try:
        response = requests.get(
            'https://api.restcountries.com/countries/v5/names.common/' + country_name,
            headers={'Authorization': 'Bearer ' + api_key}
        )
        # Check if the city was found or if permissions are valid
        if response.status_code == 200:
            # Convert raw text response into accessible Python dictionaries
            result = response.json()
            country=result
            # print(country)
            # print(json.dumps(country, indent=4))
            print(type(country))
            try:
                comm=country['data'].get('objects', {})

                if comm==[]:
                    print(f"Country '{country_name}' does not have data.")
                
                if comm:
                    # print('test')
                    for item in comm:
                        # print('test1')
                        if item.get('names', {}).get('common', '').lower() == country_name.lower():
                            # print('test2')
                            name_given = item.get('names', {}).get('common', 'N/A')
                            official_name = item.get('names', {}).get('official', 'N/A')
                            capital = item.get('capitals', ['N/A'])[0].get('name', 'N/A')
                            flag_des = item.get('flag', {}).get('description', 'N/A')
                            population = item.get('population', 'N/A')
                            region = item.get('region', 'N/A')
                            
                                    
                                        # Display results
                            print(f"--- Country Info: {name_given} ---")
                            print(f"Official Name: {official_name}")
                            print(f"Capital:       {capital}")
                            print(f"Population:    {population}")
                            print(f"Region:        {region}")
                            print(f"Flag:          {flag_des}")

            except (IndexError, KeyError) as parse_error:
                print(f"Error parsing response: {parse_error}")

        elif response.status_code == 404:
            print("\nError: The typed country could not be located. Double-check spelling.")
        else:
            print(f"\nError: Server responded with status code {response.status_code}")
            
    except requests.exceptions.RequestException as error:
        print(f"\nFailed to establish connection: {error}")

if __name__ == "__main__":
    name = input("Enter a country name: ")
    print(f"\n--- Current Status of {name} ---")
    result=get_status(name)