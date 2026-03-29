import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

class InterviewAgent:
    def __init__(self):
        # Trade-off: Swapped OpenAI for Meta's Llama-3 via Groq.
        # Result: 100% free inference and ultra-low latency.
        self.llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)
        
    def generate_first_question(self, resume_context, job_description):
        prompt = PromptTemplate(
            input_variables=["resume", "jd"],
            template="""You are an expert technical interviewer. 
            Job Description: {jd}
            Candidate's Context (From Resume): {resume}
            
            Task: Ask the very first interview question. Make it specific to their past experience and how it relates to this job role. 
            Do NOT introduce yourself, just ask the question directly."""
        )
        chain = prompt | self.llm
        response = chain.invoke({"resume": resume_context, "jd": job_description})
        return response.content
        
    def evaluate_and_respond(self, chat_history, current_answer, resume_context, job_description):
        prompt = PromptTemplate(
            input_variables=["history", "answer", "resume", "jd"],
            template="""You are an expert technical interviewer. 
            Job Description: {jd}
            Resume Context: {resume}
            
            Previous Chat History:
            {history}
            
            Candidate's Latest Answer: {answer}
            
            Task: 
            1. Briefly evaluate their answer (1-2 sentences of constructive feedback).
            2. Ask exactly one logical follow-up question based on their answer.
            Keep it professional, conversational, and strict."""
        )
        chain = prompt | self.llm
        response = chain.invoke({
            "history": chat_history, 
            "answer": current_answer, 
            "resume": resume_context, 
            "jd": job_description
        })
        return response.content