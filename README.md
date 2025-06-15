# 🤖 RAG-Powered PDF Chatbot

A beginner-friendly AI chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer questions strictly based on an uploaded PDF. Built with **Streamlit**, **LangChain**, **Groq’s LLaMA 3**, and **HuggingFace embeddings**, this project showcases how to build a smart assistant that doesn’t rely on the web — only on what *you* give it.

---

## 🚀 Features

- 📤 Upload any PDF
- 💬 Ask questions from the PDF
- 🧠 AI answers only using the provided document
- 😎 Fun manipulator persona (customizable!)
- ⚡ Fast responses via Groq LLaMA 3
- 🖥️ Clean UI with Streamlit

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – Web interface
- **LangChain** – LLM app framework
- **Groq API** – Fast inference with LLaMA 3
- **HuggingFace BGE Embeddings** – For text vectorization
- **ChromaDB** – Lightweight vector store
- **dotenv** – For managing API keys

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key
Create a .env file in the root directory:

``` ini

GROQ_API_KEY=your_groq_api_key
```
You can rename .env.example to .env and fill in your key.

### 4. Run the app
```bash
streamlit run app.py
```

## 📁 Project Structure
```bash
rag-pdf-chatbot/
├── app.py               # Main Streamlit app
├── requirements.txt     # Project dependencies
├── .env.example         # Example environment config
├── README.md            # Project overview
├── docs/                # Optional: screenshots or demo
└── uploaded_docs/       # Folder for your PDFs
```

## 🎬 Demo
https://www.linkedin.com/posts/aawhanvyas_ai-python-langchain-activity-7339601558700969984-I5at?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADaRDxMBlgfFkMQLV1Rpkmjb4yG3lBUiSjs


## 💡 How it Works
The chatbot uses RAG (Retrieval-Augmented Generation) — it breaks down your PDF into chunks, embeds them using HuggingFace, stores them in a vector database, and then uses Groq’s LLaMA 3 model to answer your questions based on what it finds in the PDF. No hallucinations from the web — only facts from your document.

## 📜 License
This project is licensed under the MIT License.

## 🙏 Acknowledgements
Groq

LangChain

Streamlit

HuggingFace

Chroma
