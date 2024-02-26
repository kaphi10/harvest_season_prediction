import numpy as np
import streamlit as st
import pandas as pd
from pickle import load


# DATA_URL= st.secrets['DATA_URL']

#@st.cache_data
st.header('Crops Harvest season Prediction')
def load_data():
    # data= load(open('dataset.pickle','rb'))
    df = pd.read_pickle('dataset.pickle')

    return df
crop = load_data()

def load_model():
    model=load(open('decision_tree.pickle','rb'))
    scaler=load(open('scaler.pickle', 'rb'))
    return model, scaler
models, scaler =load_model()
crops = st.selectbox('Choose crop',options=['rice','maize','chickpea','kidneybeans','pigeonpeas','mothbeans','mungbean','blackgram',
                                           'lentil','watermelon','muskmelon','cotton','jute'])
country = st.selectbox('choose country', options=['Nigeria','South Africa','Kenya','Sudan'])

temprature = st.number_input('Enter the temperature', min_value=9.0, max_value= 40.0)
ph = st.number_input('Enter the ph of the location', min_value=3.0, max_value=10.0)
humidity = st.number_input('Enter humidity', min_value= 14.0, max_value = 100.0)
water= st.number_input('Enter the water availability', min_value= 20.0, max_value= 300.0)

user_input= [crops, country, temprature,ph, humidity, water]
st.write(f"the input values are {user_input}".format())

label_blackgram, label_chickpea,label_cotton,label_jute,label_kidneybeans,label_lentil,label_maize,label_mothbeans,label_mungbean,label_muskmelon,label_pigeonpeas,label_rice,label_watermelon= 0,0,0,0,0,0,0,0,0,0,0,0,0
if crops == 'blackgram':
    label_blackgram = 1
elif crops == 'chickpea':
    label_chickpea=1
elif crops == 'cotton':
    label_cotton=1
elif crops == 'jute':
    label_jute =1
elif crops =='kidneybeans':
    label_kidneybeans = 1
elif crops== 'lentil':
    label_lentil =1
elif crops == 'maize':
    label_maize = 1
elif crops =='mothbeans':
    label_mothbeans = 1
elif crops == 'mungbean':
    label_mungbean = 1
elif crops =='muskmelon':
    label_muskmelon = 1
elif crops == 'pigeonpeas':
    label_pigeonpeas = 1
elif crops =='rice':
    label_rice = 1
elif crops =='watermelon':
    label_watermelon = 1

Country_Kenya,Country_Sudan,Country_Nigeria, Country_South_Africa= 0,0,0,0
if country =='Nigeria':
    Country_Nigeria =1
elif country =='Kenya':
    Country_Kenya =1
elif country=='Sudan':
    Country_Sudan =1
elif country == 'South Africa':
    Country_South_Africa =1
label_value= {'rainy': 0, 'winter': 3, 'spring': 1, 'summer': 2}
label_val_re={0:'rainy', 3:'winter',1:'spring',2:'summer'}
correct_order={0:'rainy',1:'spring',2:'summer',3:'winter'}
if st.button('Predict'):

    user_value= [[temprature,ph,humidity,water,label_blackgram,label_chickpea,label_cotton,label_jute,label_kidneybeans,
                label_lentil,label_maize,label_mothbeans,label_mungbean,label_muskmelon,label_pigeonpeas,
                label_rice,label_watermelon,Country_Sudan,Country_Nigeria,Country_South_Africa,Country_Kenya]]
    user_value= scaler.transform(user_value)
    user_value_asray = np.array(user_value)
    user_value_reshape=user_value_asray.reshape(1,-1)

    new_prediction=models.predict(user_value_reshape)
    predicted_season = crop[new_prediction][0]
    if predicted_season == 0:
        st.write('The predicted harvest period is rainy')
    elif predicted_season == 1:
        st.write('The predicted harvest period is spring')
    elif  predicted_season ==2:
        st.write('The predicted harvest period is summer')
    elif predicted_season ==3:
        st.write('The predicted harvest period is winter')
