from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai


# os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) #here we are setting the api key 

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')# loading the model 
    response = model.generate_content(question)# using generate_content we are passing question and response is stored in response and we are returning that response 
    return response.text




##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")
input=st.text_input("Input: ",key="input")



submit=st.button("Ask the question")



## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)