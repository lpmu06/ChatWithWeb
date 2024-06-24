'''
streamlit==1.30.0
pip install langchain==0.1.4
pip install langchain_openai==0.0.5 
conda install anaconda::beautifulsoup4
pip install python-dotenv
'''

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_response(user_input):
    return "I don't know"

def get_vectorstore_from_url(url):
    # get the text in document form
    loader = WebBaseLoader(url)
    document = loader.load()

    # split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # create a vectorstore from the chunks
    vector_store = Chroma.from_documents(document_chunks, OpenAIEmbeddings())    
    
    return document_chunks

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

if website_url is None or website_url == "":
    st.info("Please, enter a website URL")

else:
    document_chunks = get_vectorstore_from_url(website_url)
    #with st.sidebar:
    #    st.write(document_chunks)

    # User input
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

#    with st.sidebar:
#        st.write(st.session_state.chat_history)

    #conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

st.write("")
