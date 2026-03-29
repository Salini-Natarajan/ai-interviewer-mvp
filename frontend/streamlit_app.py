import streamlit as st
import sys
import os

# Ensure the app can find our backend modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.rag import InterviewContextManager
from app.core.agents import InterviewAgent

# --- Initialize Backend ---
@st.cache_resource
def get_managers():
    return InterviewContextManager(), InterviewAgent()

rag_manager, agent = get_managers()

# --- Page Configuration ---
st.set_page_config(page_title="AI Interviewer MVP", page_icon="🧠", layout="wide")

# --- Initialize Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Upload your resume and the job description in the sidebar to begin."}]
if "interview_active" not in st.session_state:
    st.session_state.interview_active = False
if "resume_context" not in st.session_state:
    st.session_state.resume_context = ""

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Setup")
    job_description = st.text_area("Job Description", height=150)
    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    
    if st.button("Start Interview", type="primary") and uploaded_resume and job_description:
        with st.spinner("Processing documents & building Vector DB..."):
            # 1. Extract text
            resume_text = rag_manager.extract_text_from_pdf(uploaded_resume)
            # 2. Build ChromaDB Vector Store
            rag_manager.build_vector_database(resume_text, job_description)
            # 3. Retrieve top context
            st.session_state.resume_context = rag_manager.retrieve_relevant_info("What are the candidate's core technical skills?")
            
            # 4. Generate first question
            first_q = agent.generate_first_question(st.session_state.resume_context, job_description)
            
            # 5. Update Chat
            st.session_state.messages = [{"role": "assistant", "content": first_q}]
            st.session_state.interview_active = True
            st.session_state.job_description = job_description
            st.rerun()

# --- Main Chat ---
st.title("🧠 AI Interviewer")

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if st.session_state.interview_active:
    if prompt := st.chat_input("Type your answer..."):
        # Show user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Get AI Response
        with st.chat_message("assistant"):
            with st.spinner("Evaluating..."):
                # Convert history to a string for the prompt
                history_str = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[:-1]])
                
                response = agent.evaluate_and_respond(
                    history_str, 
                    prompt, 
                    st.session_state.resume_context, 
                    st.session_state.job_description
                )
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})