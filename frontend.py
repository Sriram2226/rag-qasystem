import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Backend endpoint
BACKEND_URL = "http://127.0.0.1:8000/ask"

st.title("Retrieval-Augmented Generation (RAG) QA System")
st.write("Enter a question and get answers from the RAG-based system.")

question = st.text_input("Enter your question:")
if st.button("Submit"):
    if question.strip():
        try:
            # Send request to backend
            response = requests.post(BACKEND_URL, json={"question": question})
            if response.status_code == 200:
                st.success("Answer: ")
                st.write(response.json().get("answer", "No answer received."))
            else:
                st.error("Error: " + response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid question.")
