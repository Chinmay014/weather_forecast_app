import os,requests


api_key = os.getenv("OPENWEATHER")

def get_forecast_data(place,days): 
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    num_values = 8*days
    filtered_data = filtered_data[:num_values]
    return filtered_data


def generate_images_from_list(sky_cond):
    image_list=[]
    for data in sky_cond:
        match data:
            case "Clouds":
                image_list.append("images/cloud.png")
            case "Clear":
                image_list.append("images/clear.png")
            case "Rain":
                image_list.append("images/rain.png")
            case "Snow":
                image_list.append("images/snow.png")
    return None
            
if __name__=="__main__":
    print("HI")
    print(get_forecast_data(place="Gothenburg",days=2))