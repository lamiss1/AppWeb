import streamlit as st 



st.title("Dall-e3")
st.write ("Veuillez entrez une description de l´image ")
Description = st.text_input("tapez votre description")




#sidebar 
st.sidebar.title("Lamiss Chekh")
key = st.sidebar.text_input("tapez votre key")

key= OpenAI.api_key


# Testez ici plusieurs variation du prompte
prompt = Description



image = openai.Image.generate(
    model="dall-e-2",
    prompt=Description,
    size="512x512",
    quality="standard",
    n=1,
)

st.image.image_url = image.data[0].url








