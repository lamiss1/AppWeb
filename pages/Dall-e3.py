import streamlit as st 
from openai import OpenAI

st.title("Dall-e3")
st.write ("Veuillez entrez une description de l´image ")
Description = st.text_input("tapez votre description")




#sidebar 
st.sidebar.title("Lamiss Chekh")
key = st.sidebar.text_input("tapez votre key")








