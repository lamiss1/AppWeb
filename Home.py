import streamlit as st 

st.title("Mon formulaire")

#Text 
st.write("ceci est un formulaire de contact")

#champs de saisie 

user_input = st.text_input("tapez votre texte")

st.write (user_input)
