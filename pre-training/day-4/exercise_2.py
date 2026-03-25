import sys
import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle: Light",
    53: "Drizzle: Moderate",
    55: "Drizzle: Dense",
    61: "Rain: Slight",
    63: "Rain: Moderate",
    65: "Rain: Heavy",
    71: "Snow: Slight",
    73: "Snow: Moderate",
    75: "Snow: Heavy",
    80: "Rain showers: Slight",
    81: "Rain showers: Moderate",
    82: "Rain showers: Violent",
    95: "Thunderstorm: Slight",
    99: "Thunderstorm: Heavy hail"
}

def get_coordinates(city_name):
    try:
        response = requests.get(GEOCODE_URL, params={"name": city_name, "count": 1})
        print(response.url)
        if response.status_code != 200:
            print("Error fetching coordinates.")
            return None
        data = response.json()
        if "results" not in data or len(data["results"]) == 0:
            print("City not found.")
            return None
        result = data["results"][0]
        return result["latitude"], result["longitude"], result["name"]
    except requests.exceptions.RequestException:
        print("Network error while fetching coordinates.")
        return None

def get_weather(lat, lon):
    try:
        response = requests.get(WEATHER_URL, params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        })
        print(response.url)
        if response.status_code != 200:
            print("Error fetching weather.")
            return None
        data = response.json()
        return data.get("current_weather")
    except requests.exceptions.RequestException:
        print("Network error while fetching weather.")
        return None

def display_weather(city_name, weather):
    temp_c = weather["temperature"]
    temp_f = temp_c * 9/5 + 32
    wind = weather["windspeed"]
    code = weather["weathercode"]
    description = WEATHER_CODES.get(code, "Unknown")

    print(f"\nWeather for {city_name}:")
    print(f"Temperature: {temp_c}°C / {temp_f:.1f}°F")
    print(f"Wind Speed : {wind} km/h")
    print(f"Condition  : {description}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city_name>")
        return

    city_name = sys.argv[1]

    coords = get_coordinates(city_name)
    if not coords:
        return

    lat, lon, proper_city_name = coords

    weather = get_weather(lat, lon)
    if not weather:
        return

    print(weather)

    display_weather(proper_city_name, weather)


main()
