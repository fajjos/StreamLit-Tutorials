import streamlit as st 
import pandas as pd

st.title("Registration Form ")

first, last= st.columns(2)

first.text_input("First Name:")
last.text_input("Last Name:")

email, mob = st.columns([2,1])

email.text_input("Enter your valid E-mail address: ")
mob.text_input("Enter your valid Mobile Number: ")

username, password, retypepassword = st.columns([2, 1, 1])
username.text_input("Enter your Username: ")
password.text_input("Enter your Password: ", type="password")
retypepassword.text_input("Re-enter your Password: ", type="password")

ch, bl, sub = st.columns(3)
ch.checkbox("I agree to the terms and conditions")
sub.button("Submit")
 