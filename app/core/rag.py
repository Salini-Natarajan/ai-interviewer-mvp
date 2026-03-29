import os
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

class InterviewContextManager:
    def __init__(self):
        # Trade-off: Running embeddings locally saves 100% of API costs 
        # and keeps resume data completely private.
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = None

    def extract_text_from_pdf(self, uploaded_file):
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    def build_vector_database(self, resume_text, job_description):
        full_context = f"--- CANDIDATE RESUME ---\n{resume_text}\n\n--- TARGET JOB DESCRIPTION ---\n{job_description}"
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_text(full_context)
        
        self.vector_store = Chroma.from_texts(
            texts=chunks, 
            embedding=self.embeddings,
            collection_name="interview_data"
        )
        return True
        
    def retrieve_relevant_info(self, query, k=3):
        if not self.vector_store:
            return "No context loaded."
        docs = self.vector_store.similarity_search(query, k=k)
        return "\n\n".join([doc.page_content for doc in docs])