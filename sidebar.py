import streamlit as st 
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
import time

plt.style.use("ggplot")

data = {
    "num": [x for x in range (1,11)],
    "square": [x**2 for x in range (1,11)],
    "twice": [x*2 for x in range (1,11)],
    "thrice": [x*3 for x in range (1,11)]

}

rad = st.sidebar.radio("navigation", ["Home", "About Us"])

if rad == "Home":
          df = pd.DataFrame(data= data)
          col= st.sidebar.multiselect("Select a Column", df.columns)

          plt.plot(df['num'], df[col])

          st.pyplot()
      
     
    


if rad == "About Us":
    progress = st.progress(0)
    for i in range (100):
           time.sleep(0.1)
           progress.progress(i+1)

    st.balloons()


    st.write("You are here in about Us page ")
#status messages ->
    st.error("error")
    st.success("Show Success")
    st.info("Information ")
    st.exception(RuntimeError("This is an Error"))
    st.warning("This is a Warning ")