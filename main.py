import streamlit as st
import os
from note_pipeline import process_document, get_answer

# Set Streamlit page config
st.set_page_config(page_title="NoteNinja 🧠", page_icon="🧠", layout="centered")

# --------------------- CSS Styling ---------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        background: url('https://images.unsplash.com/photo-1522199873711-ebf3f62d0a5a?auto=format&fit=crop&w=1950&q=80') no-repeat center center fixed;
        background-size: cover;
        color: #f4f4f4;
    }

    .main {
        background: rgba(0, 0, 0, 0.55);
        backdrop-filter: blur(12px);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.4);
        margin-top: 40px;
    }

    .block-container {
        max-width: 750px;
        margin: auto;
    }

    h1, h4 {
        color: #ffffff;
        text-align: center;
    }

    .chat-box {
        background-color: rgba(255, 255, 255, 0.1);
        border-left: 4px solid #4B8BBE;
        padding: 15px 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 1.05rem;
    }

    .custom-uploader .stFileUploader {
        background-color: rgba(255,255,255,0.1);
        border: 2px dashed #4B8BBE;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        color: #ddd;
        transition: 0.3s;
    }

    .custom-uploader .stFileUploader:hover {
        background-color: rgba(255,255,255,0.2);
        border-color: #63c0f5;
    }

    input[type="text"] {
        border-radius: 10px;
        padding: 12px;
    }

    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --------------------- Header ---------------------
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("""
    <h1>🧠 NoteNinja</h1>
    <h4>Ask your PDF documents anything – Smart, Simple, Fast</h4>
    <hr style='border: 1px solid #444;'>
""", unsafe_allow_html=True)

# --------------------- File Upload Section ---------------------
st.markdown("<h2 style='text-align:center;'>📤</h2>", unsafe_allow_html=True)
st.markdown("<div class='custom-uploader'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Drag & drop or click to browse your PDF file", type=["pdf"])
st.markdown("</div>", unsafe_allow_html=True)

# --------------------- Document Processing ---------------------
vectorstore = None
if uploaded_file is not None:
    with st.spinner("🔧 Indexing your document..."):
        file_path = os.path.join("data", uploaded_file.name)
        try:
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✅ File uploaded and processed successfully.")
            vectorstore = process_document(file_path)
        except Exception as e:
            st.error(f"❌ Error processing file: {e}")

# --------------------- Chat Input & Answer ---------------------
if vectorstore:
    query = st.text_input("💬 Ask a question about your document:")

    if query:
        with st.spinner("🤖 Thinking..."):
            try:
                answer = get_answer(vectorstore, query)
                st.markdown(f"<div class='chat-box'><b>🗨️ You asked:</b> {query}<br><br><b>📎 Answer:</b><br>{answer}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Failed to get answer: {e}")

# --------------------- Footer ---------------------
st.markdown("""
    <hr style='border: 1px solid #444;'>
    <div style='text-align: center; font-size: 13px; color: #ccc;'>
        💡 Built with Streamlit + LangChain + HuggingFace<br>
        <i>NoteNinja &copy; 2025</i>
    </div>
</div>
""", unsafe_allow_html=True)
