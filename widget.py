import streamlit as st 

st.title("WIDGETS")
if st.button("Subscribe"):
    st.write("like this video too")

name = st.text_input("Name")
st.write(name)

address = st.text_area("Enter your address: ")
st.write(address)

st.date_input("enter a date:")
# st.write(date)

st.time_input("Enter a time:")

if st.checkbox("you accept the T&C", value= False):
    st.write("you have accepted the T&C")

v1= st.radio("colors",["r", "g", "b"],index=1)

v2= st.selectbox("colors",["r", "g", "b", "j"],index=1)
st.write(v1, v2,)

V3= st.multiselect("colors",["r", "g", "b"])
st.write( V3)

V4= st.slider("age", min_value=18, max_value=55, value=30, step=2)
st.write(V4)

st.number_input("numbers:", min_value=18.0, max_value=55.0, value=30.0, step=2.0)

img = st.file_uploader("Upload A File ")
st.image(img)