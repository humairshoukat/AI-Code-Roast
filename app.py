from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Streamlit page
st.set_page_config(page_title="Code Roast By AI", page_icon="🐛")

# UI for the app
st.title("Code Roast By AI 🔥")
st.write(
    "Get your code roasted by AI and learn how to write better code. "
)

# Get user input
prompt = st.text_area(
    "",
    height=275,
    placeholder="Paste your code here...",
)

# Process user input
llm = OpenAI(temperature=0.7, openai_api_key=os.getenv('OPENAI_API_KEY'))

# Roast Statement
statement = str(os.getenv('STATEMENT'))

prompt_template = PromptTemplate(
    input_variables=['code'],
    template= '{statement} {code}'
)

chain = LLMChain(llm=llm, prompt=prompt_template)

if prompt:
    with st.spinner("Roasting your code..."):
        try:
            response = chain.run(code=prompt)
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred")
