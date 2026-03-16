import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

st.set_page_config(page_title="PuppetGPT", page_icon="🤖")
st.title("🤖 PuppetGPT")
st.write("Upload a PDF and ask questions about it.")

# -------------------------
# Upload PDF
# -------------------------

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:

    os.makedirs("uploaded_docs", exist_ok=True)

    pdf_path = os.path.join("uploaded_docs", uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

# -------------------------
# Vectorstore Builder
# -------------------------

@st.cache_resource
def get_vectorstore(pdf_path):

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vectorstore

# -------------------------
# QA Chain
# -------------------------

def get_qa_chain(pdf_path):

    vectorstore = get_vectorstore(pdf_path)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k":4}
    )

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain

# -------------------------
# Chat Interface
# -------------------------

if uploaded_file:

    prompt = st.chat_input("Ask a question about the PDF...")

    if prompt:

        qa_chain = get_qa_chain(pdf_path)

        result = qa_chain.invoke({"query": prompt})

        answer = result["result"]

        st.write("### Answer")
        st.write(answer)

        with st.expander("Sources"):
            for doc in result["source_documents"]:
                st.write(doc.metadata)