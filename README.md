# 🧠 NoteNinja: Chat with Your Notes (PDF Q&A Bot)

NoteNinja is a smart chatbot that lets you **ask questions from your PDF notes** and get instant, accurate answers. It's built using **Streamlit**, **LangChain**, **FAISS**, and **Hugging Face Transformers** — making it perfect for students, researchers, and note-takers who want fast information retrieval from documents.

---

## 🚀 Features

- 📄 Upload any PDF file and index it
- 🤖 Ask natural language questions about the document
- 🔍 Fast and context-aware answers using Hugging Face models
- 🧠 Embedding + retrieval powered by FAISS and LangChain
- 💡 Clean UI with Streamlit

---

## 📦 Tech Stack

- **Streamlit** – for the front-end UI
- **LangChain** – for managing the retrieval-augmented pipeline
- **FAISS** – for efficient similarity search
- **Hugging Face Transformers** – for question-answering models
- **Python-dotenv** – to manage API keys securely

---

## ⚙️ Setup Instructions

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/BHANUKONTHAM-1109/NoteNinja.git
cd NoteNinja

2. Install Dependencies
pip install -r requirements.txt

3. Set Up Environment Variables
Create a .env file in the root folder and add your Hugging Face key:

HUGGINGFACE_API_KEY=your_huggingface_key

4. Run the App
 streamlit run main.py