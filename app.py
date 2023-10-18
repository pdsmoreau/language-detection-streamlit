import streamlit as st
import requests

def make_request(payload):
    r = requests.post('https://language-detection-app.onrender.com/predict/', json=payload)
    
    if r.status_code == 200:
        prediction = r.json()
        return prediction['language']
    else:
        return None

st.title("Language Detection APP")


text = st.text_area("Enter here the text you want to discover the language:")


if st.button("What is the language?"):
    if text:
        payload = {
            "text": text
        }
        
        prediction = make_request(payload)
        
        if prediction:
            st.write(f"The language of the text is: {prediction}")
    else:
        st.write("Please, enter the text to discover the language.")