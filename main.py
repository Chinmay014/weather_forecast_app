import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next days")
# st.write("Place:")

place = st.text_input("Place:")

# st.text("Forecast days")
days = st.slider("Forecast days",min_value=1,max_value=5,help="Select the number of days in future")

option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")