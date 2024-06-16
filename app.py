from dotenv import load_dotenv
load_dotenv() ## loadimg all env vars

import streamlit as st
import os 
import pathlib
import textwrap
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## func to load gemini pro

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#inituialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Pro Application")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask The question")

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is ...")
    st.write(response)

