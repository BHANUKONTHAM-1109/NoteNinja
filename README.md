# 🧠 NoteNinja - Chat with Your Notes (PDF Q&A Bot)

NoteNinja is a powerful PDF Question-Answering assistant that allows users to upload a PDF and interact with its content using natural language. It leverages LangChain, FAISS, Hugging Face Transformers, and Streamlit to provide accurate and responsive answers from document content.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🤖 Ask natural language questions from the content
- 🔍 Embedding-based document search with FAISS
- 🧠 Response generation via Hugging Face Transformers
- ⚙️ Simple and fast interface built with Streamlit
- 🔐 Secure API key handling via `.env`

---

## 🛠️ Tech Stack

| Layer         | Tech Used                     |
|---------------|-------------------------------|
| Frontend      | Streamlit                     |
| Backend Logic | LangChain, Python             |
| Vector DB     | FAISS                         |
| NLP Models    | Hugging Face Transformers     |
| File Parsing  | PyPDF2                        |
| Secrets Mgmt  | python-dotenv                 |

---

## 📦 Installation

### 1. Clone the Repository

git clone https://github.com/BHANUKONTHAM-1109/NoteNinja.git
cd NoteNinja

2. Create a Virtual Environment (optional)
python -m venv venv
# Activate the venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Configure API Key
Create a .env file in the root directory:

env
HUGGINGFACE_API_KEY=your_huggingface_token_here
⚠️ Your .env file is included in .gitignore and will not be uploaded to GitHub.

🚀 Run the App
streamlit run main.py

📁 Folder Structure

NoteNinja/
├── main.py
├── requirements.txt
├── .env               
├── .gitignore
├── README.md
└── utils/              
💬 Example Use Case
Upload your class notes PDF

Ask: "What is the definition of entropy in this document?"

Get instant, context-aware answers extracted from your PDF

📸 Screenshots


Upload PDF	Ask a Question	Get Answers

🌍 Deploy on Streamlit Cloud
Push your code to GitHub

Go to https://streamlit.io/cloud

Click "Deploy App"

Set the app path: main.py

Add secret environment variable:
HUGGINGFACE_API_KEY=your_token_here
Click Deploy

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Contributions are welcome!
Please fork the repository and submit a pull request.

👤 Author
Bhanu Kontham
🔗 GitHub: @BHANUKONTHAM-1109
