# 🤖 PuppetGPT — Chat With Your Documents

PuppetGPT is a **Retrieval-Augmented Generation (RAG) powered document assistant** that allows users to upload a PDF and ask questions about its contents.

Instead of relying only on the language model’s internal knowledge, PuppetGPT retrieves relevant sections from the document using semantic search and feeds them to the LLM to generate accurate, grounded responses.

Built with **LangChain, Groq LLaMA models, Chroma vector database, and Streamlit**, this project demonstrates how modern AI applications combine **retrieval systems with large language models** to build reliable document assistants.

---

# 🎭 Why the Name *PuppetGPT*?

Most LLMs generate responses freely based on their training data, which can sometimes result in hallucinations or incorrect answers.

PuppetGPT takes a different approach.

Instead of letting the model respond freely, the system **guides the LLM using retrieved document context**. The retrieved chunks act like **strings controlling the model’s responses**, ensuring answers remain grounded in the document.

In simple terms:

```
Document Context (strings)
        ↓
Retriever pulls relevant chunks
        ↓
LLM generates grounded response
        ↓
Accurate Answer
```

Just like a puppet moves according to the strings controlling it, **the language model generates answers based on the document context provided**.

This design significantly improves **accuracy, reliability, and transparency**.

---

# 🚀 Features

📄 **Upload Any PDF**
Upload any document and instantly start querying it.

🧠 **Retrieval-Augmented Generation (RAG)**
Responses are generated using retrieved document context.

⚡ **Fast LLM Responses**
Powered by **Groq’s ultra-fast LLaMA models**.

🔍 **Semantic Document Search**
Embeddings + vector similarity search retrieve relevant document chunks.

📚 **Source Transparency**
Shows which document sections were used to generate the answer.

🖥 **Interactive Streamlit Interface**
Clean and simple UI for chatting with documents.

---

# 🧠 System Architecture

```
User Uploads PDF
        ↓
Document Loader
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
Chroma Vector Database
        ↓
Semantic Retrieval (Top-K)
        ↓
Prompt Construction
        ↓
Groq LLaMA Model
        ↓
Answer + Sources
```

This architecture improves **accuracy, contextual relevance, and trustworthiness** compared to traditional LLM responses.

---

# 🛠 Tech Stack

| Component       | Technology                        |
| --------------- | --------------------------------- |
| Frontend        | Streamlit                         |
| Framework       | LangChain                         |
| LLM             | Groq LLaMA                        |
| Embeddings      | HuggingFace Sentence Transformers |
| Vector Database | ChromaDB                          |
| Language        | Python                            |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aawhan0/PuppetGPT.git
cd PuppetGPT
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup API Key

Create a `.env` file in the project root and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

You can obtain a key from:

https://console.groq.com

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

Upload a PDF and start chatting with your document.

---

# 📂 Project Structure

```
PuppetGPT
│
├── app.py                # Streamlit interface
├── ingest.py             # Document ingestion pipeline
├── rag_pipeline.py       # Retrieval + LLM logic
├── requirements.txt
├── README.md
│
├── uploaded_docs/        # Uploaded PDFs
├── vectorstore/          # Chroma vector database
```

---

# 📊 Key Concepts Demonstrated

This project demonstrates important AI engineering concepts:

* Retrieval-Augmented Generation (RAG)
* Semantic search using embeddings
* Vector databases
* Prompt grounding
* LLM integration with external knowledge
* Document-based AI assistants

---

# 🌟 Example Use Cases

• Chat with research papers
• Extract insights from reports
• Query technical documentation
• Summarize books or PDFs
• Build internal knowledge assistants

---

# 🔮 Future Improvements

* Multi-document retrieval
* Hybrid search (BM25 + embeddings)
* Conversation memory
* Streaming responses
* Evaluation metrics dashboard

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🙌 Acknowledgements

* LangChain
* Groq
* HuggingFace
* Chroma
* Streamlit

---

⭐ If you found this project useful, consider giving it a star!
