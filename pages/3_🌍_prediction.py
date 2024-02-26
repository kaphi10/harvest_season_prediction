import streamlit as st
import pandas as pd
import numpy as np
from home_page import load_data

st.set_page_config(page_title= "crop prediction App", page_icon="🌍")
from pickle import load
st.sidebar.header("Harvest Season Prediction")
st.subheader('Predicting Harvest Season of the crops')
def load_encoded():
    df_encoded=pd.read_csv('encoded_data1.csv')
    return df_encoded
def load_model():
    model= load(open(r'C:\Users\HP\Desktop\Hakathon\decision_tree.pickle','rb'))
    scaler=load(open(r'C:\Users\HP\Desktop\Hakathon\scaler.pickle', 'rb'))
    return model,scaler
df=load_data()
df_encoded=load_encoded()
plant = st.selectbox('select crop', (sorted(df.label.unique())))
updated = df.loc[df['label'] == plant]
country= st.selectbox('select Country', (sorted(updated.Country.unique())))
updated = updated.loc[updated['Country'] == country]
temprature = st.number_input('Enter the temperature', min_value=9.0, max_value= 40.0)
ph = st.number_input('Enter the ph of the location', min_value=3.0, max_value=10.0)
humidity = st.number_input('Enter humidity', min_value= 14.0, max_value = 100.0)
water= st.number_input('Enter the water availability', min_value= 20.0, max_value= 300.0)

country_option=[]
crop_option=[]
for region in  updated.Country.unique():
    update=updated.loc[updated['Country']== region]
    for crop in updated.label.unique():
        update2= updated.loc[updated['label'] == crop]
        country_option.append(region)
        crop_option.append(crop)


test = pd.DataFrame({'temperature':temprature, 'ph': ph, 'humidity': humidity, 'water availability': water,'Country':country_option,'label':crop_option})
test_decoded=pd.DataFrame(0, index=np.arange(len(crop_option)), columns=df_encoded.columns.values)
record = pd.DataFrame()
# test['temperature']=temprature
record['temperature']=temprature
# test['ph']=ph
record['ph']=ph
# test['humidity']=humidity
record['humidity']=humidity
# test['water availability']=water
record['water availability']=water
# test['Country']=country_option
record['Country']=country_option
# test['label']=crop_option
record['label']=crop_option


dummies_col = pd.get_dummies(test, columns=['Country', 'label'])
#dummies_col= dummies_col.loc[:, ~dummies_col.T.duplicated(keep='first')]

other_col= test_decoded.loc[:, ~test_decoded.columns.isin(dummies_col.columns)]
final_test_col=pd.concat([dummies_col,other_col], axis=1)
final_test_col.drop(columns=['season','encoded_season'], inplace=True)
# st.write(final_test_col)
label_value= {'rainy': 0, 'winter': 3, 'spring': 1, 'summer': 2}
label_val_re={0:'rainy', 3:'winter',1:'spring',2:'summer'}
correct_order={0:'rainy',1:'spring',2:'summer',3:'winter'}
if st.button('Predict'):

    model, scaler =load_model()
    test_scaled=scaler.transform(final_test_col.values)
    prediction=model.predict(test_scaled)

    # st.write(prediction)
    test['predicted']=prediction
    test['predicted']= test['predicted'].map(correct_order)
    #st.write(test)
    predicted_value=list(test.predicted)

    #Let convert the list to string for readability
    def listToString(text):
        # initialize an empty string
        str1 = ""
        # traverse in the string
        for ele in text:
            str1 += ele
        # return string
        return str1
    # Driver code
    text = predicted_value
    st.write("The harvesting season predicted is ", listToString(text))
