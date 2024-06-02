import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import altair as alt #pip install altair

data = pd. DataFrame(
    np.random.randn(100, 3),
    columns = ['a', 'b', 'c']

)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a', y = 'b', tooltip=['a', 'b']
)

st.map()
st.graphviz_chart("""
digraph{
hello -> hi
hi -> hola
hola -> amigo 
hola -> hello
}""") #for flow charts 


st.altair_chart(chart, use_container_width=True)

plt.scatter(data['a'],data['b'])
plt.title("scatter")
st.pyplot()

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)

st.image("data//sal.png", width=400)
st.audio("")
st.video("")
