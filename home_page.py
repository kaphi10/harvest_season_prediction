import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title= "crop prediction App", page_icon="🏘️" )
st.image('rice-farm.jpg', caption='Rice plantation')
def load_data():
    df= pd.read_csv('Crop_Data.csv')
    return df
df=load_data()
st.title("Harvest Season :red[Prediction]")
st.markdown("The application is to predict the harvest season of the plant base on their region")
st.write("""The purpose of the project is to predict the harvesting period of some crops in Africa, using water availability, Humidity, soil pH, and temperature.
Looking at the dependency ratio of all independent variables, Water availability, and Humidity play a vital role in the harvesting season prediction according to regions.
The label or dependent variable in the dataset is harvest season, and the countries include, Nigeria, South Africa, Kenya, and Sudan, with four harvest seasons which include rainy, winter, summer, and spring.
The table below shows a sample dataset used for the model training."""
)
st.write(df.head(10))