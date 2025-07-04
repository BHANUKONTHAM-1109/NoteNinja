from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import os

def process_document(file_path):
    try:
        if not os.path.exists(file_path):
            print("❌ File path does not exist.")
            return None

        loader = PyPDFLoader(file_path)
        documents = loader.load()

        if not documents:
            print("❌ No documents loaded from PDF.")
            return None

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = splitter.split_documents(documents)

        if not docs:
            print("❌ Document splitting failed.")
            return None

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.from_documents(docs, embeddings)

        return vectorstore

    except Exception as e:
        print(f"❌ Exception in process_document: {e}")
        return None


def get_answer(vectorstore, query):
    try:
        docs = vectorstore.similarity_search(query)

        model_name = "google/flan-t5-base"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

        llm = HuggingFacePipeline(pipeline=pipe)

        chain = load_qa_chain(llm, chain_type="stuff")
        answer = chain.run(input_documents=docs, question=query)
        return answer

    except Exception as e:
        return f"❌ Failed to get answer: {e}"
