import streamlit as st 
import pandas as pd
import numpy as np 
import time


a = [1, 2, 3, 4, 5, 6, 7, 8 ]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":"faiz",
    "age":20,
    "city":"aligarh",
}

data = pd.read_csv("data//Salary_Data.csv")
st.dataframe(nd)
st.dataframe(dic)
st.dataframe(data, width=500, height=400)

st.table(data) # in this case we dont get the scroll bar but the whole data, basically used for smaller data 
st.json(dic)
st.write(data) 

@st.cache            #caching basically used for faster processing of the data 
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1 "):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))