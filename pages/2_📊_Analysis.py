import streamlit as st
from home_page import load_data
st.set_page_config(page_title= "Analysis", page_icon="📊" )

st.sidebar.header("Crop analysis")
st.subheader("This page give a brief analysis base on region")
df=load_data()
region_tocheck= sorted(df.Country.unique())
option= st.selectbox("select country",(region_tocheck))
selected= df.loc[df['Country']==option]

# let analyse the crop yield by region
tab1, tab2, tab3 =st.tabs(["Most planted crop in a region",
                           "Rarely planted crops in the region",
                           "Rainfall per region"])
crop_yield= selected["label"].value_counts()
water=selected.groupby(["label"])[['water availability']].sum().sort_values(by=['water availability'], axis=0, ascending=False)

tab1.subheader(f"The most cultivated crop in the {option}")
tab1.bar_chart(crop_yield.head(5), height=500, color='#F7D53D')

tab2.subheader(f"The Least cultivated crop in the {option}")
tab2.bar_chart(crop_yield.tail(5), height=500, color='#F7D53D')

tab3.subheader(f"Water availability to cultivate each crop in the {option}")
tab3.bar_chart(water, height=500, color='#F7D53D')
tab3.subheader(f"Detail analysis of the numerical independent variable in {option}")
tab3.write(selected.describe())