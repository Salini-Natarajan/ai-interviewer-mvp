# 🤖 AI Interviewer MVP

> An agentic, RAG-powered technical interview engine that knows *your* resume and *your* target job.

---

## 🧠 What It Does

Most interview prep tools are generic. This one isn't.

**AI Interviewer** ingests your specific **PDF resume** and a target **Job Description**, builds a localized memory context using vector embeddings, and deploys multiple AI agents to conduct a rigorous, real-time technical interview — complete with constructive feedback at the end.

It doesn't ask random questions. It asks *your* questions, based on *your* experience.

---

## ✨ Key Features

- 📄 **Resume-aware questioning** — reads your PDF and targets gaps and strengths
- 🎯 **JD-contextual** — aligns questions to the actual job requirements
- 🧠 **RAG memory** — uses vector search (Qdrant) for localized context retrieval
- 🤖 **Multi-agent architecture** — separate agents for questioning, evaluation, and feedback
- 💬 **Real-time conversation** — natural back-and-forth interview flow
- 📝 **Constructive feedback** — post-interview performance summary

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | Ollama (local) |
| RAG / Embeddings | LangChain + Qdrant |
| PDF Parsing | PyMuPDF / pdfplumber |
| Agent Framework | LangChain Agents |
| Backend | Python |
| Vector DB | Qdrant |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/Salini-Natarajan/ai-interviewer-mvp.git
cd ai-interviewer-mvp

# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running locally
ollama run llama3

# Run the app
python main.py
```

---

## 📁 Project Structure

```
ai-interviewer-mvp/
├── main.py              # Entry point
├── agents/              # Interview, evaluation, feedback agents
├── rag/                 # Document ingestion + vector retrieval
├── utils/               # PDF parsing, helpers
├── requirements.txt
└── README.md
```

---

## 🎯 Use Cases

- Final-year students preparing for campus placements
- Job seekers targeting specific roles
- Anyone wanting personalized, not generic, interview prep

---

## 👩‍💻 Built By

**Salini N** — AIML Student, KPR Institute of Engineering and Technology
[LinkedIn](https://linkedin.com/in/salininatarajan) · [GitHub](https://github.com/Salini-Natarajan)
