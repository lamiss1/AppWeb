import streamlit as st 

st.title("Dall-e3")
st.write ("Veuillez entrez une description de l´image ")

Description = st.text_input("tapez votre description")


# OpenAI pour générer des images
from openai import OpenAI


client = OpenAI(api_key=OpenAIKEY)


# Testez ici plusieurs variation du prompte
prompt = Description



image = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="512x512",
    quality="standard",
    n=1,
)

image_url = image.data[0].url
print(image_url)


