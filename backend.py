import os,requests


api_key = os.getenv("OPENWEATHER")

def get_forecast_data(place,days,kind=None): 
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    num_values = 8*days
    filtered_data = filtered_data[:num_values]
    if kind == "Temperature":
        filtered_data = [data_pt["main"]["temp"] for data_pt in filtered_data]
    if kind == "Sky":
        filtered_data = [data_pt["weather"][0]["main"] for data_pt in filtered_data]
    return filtered_data

if __name__=="__main__":
    print("HI")
    print(get_forecast_data(place="Kota"))