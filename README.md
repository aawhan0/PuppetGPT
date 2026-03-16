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
# 🧩 Engineering Challenges & Fixes

While building PuppetGPT, several practical engineering issues arose related to environment setup, dependency management, RAG architecture, and LLM behavior.

**1. Python Compatibility**

Issue: Streamlit Cloud defaulted to Python 3.14, causing compatibility issues with AI libraries.

Fix: Deployment environment was changed to Python 3.11, which is currently the most stable version for LangChain-based applications.

**2. LangChain Package Fragmentation**

Issue: LangChain was split into multiple packages, causing import errors.

Fix: Updated imports to the modular architecture:

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

**3. Dependency Conflicts**

Issue: Version conflicts between LangChain-related packages caused installation failures.

Fix: Rebuilt the Python virtual environment and reinstalled dependencies to ensure clean resolution.

**4. Groq Model Deprecation**

Issue: The original model llama3-8b-8192 was deprecated.

Fix: Updated to:

model_name="llama-3.1-8b-instant"

**5. RetrievalQA Memory Conflict**

Issue: LangChain memory conflicted with RetrievalQA because the chain returns multiple outputs.

Fix: Chat history was managed using Streamlit session state:

st.session_state.chat_history
**6. Vectorstore Rebuild Errors**

Issue: Rebuilding the Chroma vector database on every query caused runtime errors.

Fix: Vectorstore creation was cached so embeddings are generated once per document upload.

**7. Code Architecture Bug**

Issue: Some logic was placed after a return statement, making it unreachable.

Fix: Refactored the architecture into two functions:

get_vectorstore()
get_qa_chain()

**8. Hallucination Mitigation**

Issue: The model occasionally generated answers not present in the document.

Fix: Added a strict prompt rule requiring the model to respond:

"I cannot find this information in the document."

when the answer is not in the retrieved context.

**9. Output Formatting Issues**

Issue: The model sometimes produced compressed bullet lists.

Fix: Added a formatting step before displaying answers:

answer = answer.replace("• ", "\n• ").strip()
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
