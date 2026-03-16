import os
import shutil
import time
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

st.set_page_config(page_title="PuppetGPT", page_icon="🤖")

st.title("🤖 PuppetGPT")
st.caption("Chat with your documents using Retrieval-Augmented Generation")

# -------------------------
# Reset Conversation Button
# -------------------------

if st.button("Reset Conversation"):
    st.session_state.chat_history = []

# -------------------------
# Upload PDF
# -------------------------

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

# Show uploaded document names in UI
if uploaded_files:

    st.subheader("Loaded Documents")

    for file in uploaded_files:
        st.write("📄", file.name)

# -------------------------
# Save Uploaded Files
# -------------------------

if uploaded_files:

    # clear old data
    if os.path.exists("vectorstore"):
        shutil.rmtree("vectorstore")

    if os.path.exists("uploaded_docs"):
        shutil.rmtree("uploaded_docs")

    os.makedirs("uploaded_docs", exist_ok=True)

    # save all uploaded files
    for file in uploaded_files:

        pdf_path = os.path.join("uploaded_docs", file.name)

        with open(pdf_path, "wb") as f:
            f.write(file.read())

    st.success(f"{len(uploaded_files)} PDFs uploaded successfully!")
# -------------------------
# Vectorstore Builder
# -------------------------

def get_vectorstore(pdf_path):

    docs = []
    for file in os.listdir("uploaded_docs"):
        loader = PyPDFLoader(os.path.join("uploaded_docs", file))
        docs.extend(loader.load())

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
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    return vectorstore


# -------------------------
# Prompt Template
# -------------------------

template = """
You are a document assistant.

Answer the question ONLY using the provided context.

If the answer is not contained in the document context, say:
"I cannot find this information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

qa_prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

# -------------------------
# QA Chain
# -------------------------

def get_qa_chain(pdf_path):

    vectorstore = get_vectorstore(pdf_path)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        memory=memory,
        chain_type_kwargs={"prompt": qa_prompt},
        return_source_documents=True
    )

    return qa_chain

# -------------------------
# Chat Memory
# -------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)

# -------------------------
# Chat Interface
# -------------------------

if uploaded_files:

    user_question = st.chat_input("Ask a question about the PDF...")

    if user_question:

        st.session_state.chat_history.append(("user", user_question))

        with st.chat_message("user"):
            st.write(user_question)

        qa_chain = get_qa_chain(pdf_path)

        with st.chat_message("assistant"):

            with st.spinner("Searching document context..."):

                result = qa_chain.invoke({"query": user_question})
                answer = result["result"]

            # progressive typing effect
            placeholder = st.empty()
            typed_text = ""

            for char in answer:
                typed_text += char
                placeholder.markdown(typed_text)
                time.sleep(0.01)

        st.session_state.chat_history.append(("assistant", answer))

# -------------------------
# Show Sources
# -------------------------

with st.expander("Sources"):

    for doc in result["source_documents"]:

        source = doc.metadata.get("source", "Unknown document")
        page = doc.metadata.get("page", "Unknown")

        filename = os.path.basename(source)

        st.write(f"📄 **{filename}** (Page {page})")