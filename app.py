# phase 1 imports
import os
import streamlit as st
from dotenv import load_dotenv

# phase 2 imports
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# phase 3 imports
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA

load_dotenv()

st.title("RAG Chatbot")

#Setup a session state variable to hold all the old messages
if "messages" not in st.session_state:
    st.session_state.messages = []

#Display all the previous messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])


@st.cache_resource
def get_vectorstore():
    pdf_name= "ArtOfManipulation.pdf"
    loaders= [PyPDFLoader(pdf_name)]
    # Create Chunks, aka Vectors (ChromaDb)
    index= VectorstoreIndexCreator(
        embedding= HuggingFaceBgeEmbeddings(model_name= "BAAI/bge-small-en"),
        text_splitter= RecursiveCharacterTextSplitter(chunk_size= 1000, chunk_overlap= 100 )
    ).from_loaders(loaders)
    return index.vectorstore


prompt = st.chat_input("Pass your prompt here!")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({'role':'user', 'content':prompt})

    groq_sys_prompt = ChatPromptTemplate.from_template("""You are a master manipulator — sharp, persuasive, and always in control. 
                                                        Help the user influence others and get what they want using charm, pressure, or psychology.
                                                        No fluff. Just clever, effective strategies or messages that work.
                                                        Here’s the situation: {user_prompt}""")

    model = "llama3-8b-8192"
    groq_chat = ChatGroq(
        groq_api_key = os.environ.get("GROQ_API_KEY"),
        model_name= model
    )

    try:
        vectorstore= get_vectorstore()
        if vectorstore is None:
            st.error("Failed to load the document.")
        else:
            chain = RetrievalQA.from_chain_type(
                 llm= groq_chat,
                 chain_type= "stuff",
                 retriever= vectorstore.as_retriever(search_kwargs={"k":3}),
                 return_source_documents= True
            )
            result =chain({"query": prompt})
            response = result["result"]


            # response = "I am your Assistant!"
            st.chat_message("assistant").markdown(response)
            st.session_state.messages.append({'role':'assistant', 'content':response})

    except Exception as e:
            st.error(f"Error: [{str(e)}]")
