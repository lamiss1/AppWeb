import streamlit as st 

st.title("Mon formulaire")

#Text 
st.write("ceci est un formulaire de contact")

#champs de saisie 

user_input = st.text_input("tapez votre texte")

st.write (user_input)

#image
st.image("https://www.eemi.com/uploads/2023/06/sized/Campus-de-Paris-scaled-aspect-ratio-690-690-scaled-380x380.jpg")

#sidebar 

st.sidebar.title("Lamiss Chekh")
st.sidebar.video("https://www.youtube.com/watch?v=Bs4Acx_ugc4")

#SelectBar
student_grad= st.selectbox("  Selectionnez votre niveau d´etude", ["Bac","Bac+1","Bac+2"])

#Select Slider 
age = st.select_slider("Quel est votre age", range(0, 40))
