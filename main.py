import streamlit as st
import plotly.express as px
from backend import get_forecast_data

st.title("Weather forecast for the next days")
# st.write("Place:")
place = st.text_input("Place:")     
# st.text("Forecast days")
days = st.slider("Forecast days",min_value=1,max_value=5,help="Select the number of days in future")

option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # get data from API
    filtered_data = get_forecast_data(place,days)
    if(type(filtered_data)!=list):
        st.write(filtered_data)
    else:
        if option == "Temperature":
                temperatures = [0.1*(data_pt["main"]["temp"]) for data_pt in filtered_data]
                dates = [data_pt["dt_txt"] for data_pt in filtered_data]
                figure = px.line(x=dates,y=temperatures,labels={"x":"","y":"Temperature (C)"})
                st.plotly_chart(figure)
        if option == "Sky":
                sky_conditions = [data_pt["weather"][0]["main"] for data_pt in filtered_data]
                dates = [data_pt["dt_txt"] for data_pt in filtered_data]
                image_dict={"Clear":"images/clear.png","Clouds":"images/cloud.png",
                            "Rain":"images/rain.png","Snow":"images/snow.png"}
                image_paths = [image_dict[condition] for condition in sky_conditions]
                st.image(image_paths, width=115)