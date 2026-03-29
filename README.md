# 🧠 AI Interviewer (Real-Time Prep Engine)

**Live Demo:** 
(https://ai-interviewer-mvp-bspwk4y3zlksbkkp727ytj.streamlit.app/)

## 🚀 Overview
The AI Interviewer is an agentic, RAG-powered application designed to solve a critical problem for university students: the lack of accessible, highly tailored technical interview practice. 

Unlike generic chatbots, this engine ingests a candidate's specific PDF resume and a target Job Description, builds a localized memory context, and deploys multiple AI agents to conduct a rigorous, contextual, and real-time technical interview, complete with constructive feedback.

## 🏗️ System Architecture & Tech Stack
This MVP was built emphasizing low latency, high reasoning capabilities, and data privacy.

* **Frontend:** Streamlit (Rapid UI prototyping & state management)
* **Orchestration:** LangChain (Agentic workflows and prompt chaining)
* **Vector Database:** ChromaDB (In-memory vector storage for RAG context)
* **Embeddings:** HuggingFace `all-MiniLM-L6-v2` (Local, open-source embeddings)
* **LLM Engine:** Meta Llama 3.3 70B via Groq (Ultra-fast inference)

## ⚖️ Infrastructure Trade-Offs (Design Decisions)
During development, specific architectural pivots were made to balance cost, speed, and privacy:

1. **Local Embeddings vs. Paid APIs:** Initially tested with OpenAI's `text-embedding-3-small`. To eliminate API dependency, reduce cloud costs to $0, and ensure candidate resume data never leaves the server during the embedding process, the system was re-architected to use HuggingFace's local `all-MiniLM-L6-v2` model.
2. **Groq LPU vs. Standard GPU Cloud:** Swapped standard OpenAI models for Meta's Llama 3.3 hosted on Groq's LPU inference engine. **Trade-off:** We traded the massive ecosystem of OpenAI for the blazing-fast token generation speed of Groq, which is critical for maintaining a natural, real-time conversational flow during an interview simulation.

## 🧠 Agentic Workflow
The system operates using a localized multi-agent logic flow:
1. **The Context Manager:** Ingests the PDF and JD, chunks the text, and stores it in ChromaDB.
2. **The Recruiter Agent:** Retrieves the top-k relevant skills from the Vector DB and generates a highly specific opening question.
3. **The Evaluator Agent:** Analyzes the user's real-time chat input against the JD, provides 1-2 sentences of actionable feedback, and seamlessly generates the next logical follow-up question.

