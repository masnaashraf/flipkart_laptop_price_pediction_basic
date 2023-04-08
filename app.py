import streamlit as st
import pickle
import numpy as np
import pandas as pd
#load the model and dataframe
df = pd.read_csv("flipkart_datanew.csv")


st.header(":blue[Select the laptop specification for which you need to know the approximate price in Rupees]")




pipe = pickle.load(open("pipe.pkl", "rb"))




st.subheader("Select each specifications:")

#Now we will take user input one by one as per our dataframe
#Brand

company = st.selectbox('Brand', df['Brand'].unique())

#Operating system

os = st.selectbox('Operating System', df['Operating System'].unique())


#RAM Type

ramtype = st.selectbox('RAM Type', df['Ram Type'].unique())

#RAM Size

ramsize = st.selectbox('Ram Size', df['Ram Size'].unique())

#Disk Size

disksize = st.selectbox('Disk Size', df['Disk Size'].unique())

#Disk Type

disktype = st.selectbox('Disk Type', df['Disk Type'].unique())

data={'Brand':company,
     'Operating System':os,
     'Ram Type':ramtype,
     'Ram Size':ramsize,
     'Disk Size':disksize,
     'Disk Type':disktype}
features=pd.DataFrame(data,index=[0])
if st.button("Predict"):
    prediction = pipe.predict(features)
    predval=int(prediction[0])
    st.write(predval)
   