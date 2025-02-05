import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain_community.chat_models import ChatOllama

chat_model = ChatOllama(
    model="zephyr:7b-beta-q4_K_M",
)

# Initializing the OpenAI model
model = chat_model

# Setting up a Streamlit web app title
st.title("Story Creator")
# Text input field for the user to enter a topic
topic = st.text_input("Choose a topic to create a story about")

# Prompt template for generating a story title
prompt = PromptTemplate.from_template(
    "Write a great title for a story about {topic}"
)

# Executing the chain if the user has entered a topic
if topic:
    # Displaying a spinner while content created
    with st.spinner("Creating story title"):
        # Chain for title using model and formatting
        chain = prompt | model | StrOutputParser()
        # Invoking the chain, storing the result
        response = chain.invoke({"topic": topic})
        # Displaying the generated title
        st.write(response)


