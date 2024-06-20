'''
streamlit==1.30.0
pip install langchain==0.1.4
pip install langchain_openai==0.0.5 
'''

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input):
    return "I don't know"

# App config
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with websites")

#Persistence
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
      AIMessage(content="Hello, I am a bot, how can I help you?")
]




# Sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

# User input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    response = get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))

with st.sidebar:
    st.write(st.session_state.chat_history)




