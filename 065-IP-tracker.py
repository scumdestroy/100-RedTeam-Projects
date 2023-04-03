import requests

def get_location(ip_address, api_key):
    url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        print(data["error"]["info"])
        return None
    else:
        return data

if __name__ == "__main__":
    ip_address = input("Enter IP address to track: ")
    api_key = input("Enter ipstack API key: ")
    location_data = get_location(ip_address, api_key)
    if location_data:
        print(f"IP address: {location_data['ip']}")
        print(f"Country: {location_data['country_name']}")
        print(f"Region: {location_data['region_name']}")
        print(f"City: {location_data['city']}")
        print(f"Latitude: {location_data['latitude']}")
        print(f"Longitude: {location_data['longitude']}")
