# 🧠 Interview Voice Agent (AI Copilot for Mock Interviews)

A ChatGPT-like interview assistant with **resume grounding + bilingual support + voice input**, designed to help candidates generate **interview-ready answers in real time**.

---

## ✨ Features

- 🎤 **Voice Input (Chinese + English)**
  - Browser-based speech recognition
  - Supports Chinese, English, and mixed input

- 🧠 **Resume Injection (Grounded AI)**
  - Answers are generated based on structured resume data
  - Prevents hallucinated experience
  - Produces realistic, personalized responses

- 🌍 **Bilingual Output**
  - Spoken English (interview-ready)
  - Chinese explanation (for clarity)

- ⚡ **Streaming Responses**
  - Token-level streaming (ChatGPT-like experience)

- 💬 **Conversation Memory**
  - Maintains context within session
  - Supports follow-up questions

- 🔄 **Session Management**
  - Reset / clear chat
  - New session creation

---

## 🏗️ Architecture


Browser (Voice / Text)
↓
Speech Recognition (Web API)
↓
FastAPI Backend
↓
Resume Injection + Prompt Engineering
↓
OpenAI LLM (Streaming)
↓
Real-time Response Rendering


---

## 🛠️ Local Setup (Required)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/interview-agent.git
cd interview-agent
2️⃣ Create Python environment (recommended)
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure OpenAI API Key

You need an API key from OpenAI.

Option A: Environment variable (recommended)
export OPENAI_API_KEY=your_api_key
Option B: .env file

Create a .env file:

OPENAI_API_KEY=your_api_key

⚠️ Do NOT commit this file to GitHub

5️⃣ Prepare resume.json (IMPORTANT)

The system uses a structured resume file.

Example:

{
  "name": "Your Name",
  "skills": ["Java", "Kubernetes"],
  "projects": [
    {
      "name": "Project A",
      "tech_stack": ["Spring Boot"],
      "details": ["Built APIs"],
      "impact": "Improved performance"
    }
  ]
}

👉 This is used to ground the LLM responses

▶️ Run the Project
uvicorn main:app --reload

Open browser:

http://127.0.0.1:8000
🎤 How to Use
🧾 Text Input
Type your question
Press Enter or click Send
🎤 Voice Input
Click 🎤 Voice
Speak (Chinese / English / mixed)
Click Stop
Input auto-fills and sends
🔄 Clear Chat
Click Clear
Resets:
UI messages
backend session
conversation memory
🧠 Prompt Strategy

This project uses advanced prompt engineering:

Resume-grounded responses
Bilingual output format
Anti-hallucination rules
Fallback when uncertain

Example:

[Keywords]
- Kubernetes
- HPA

[Answer - English]
In Kubernetes, HPA automatically scales pods...

[Answer - 中文]
Kubernetes 的 HPA 是一种自动扩缩容机制...
⚙️ Tech Stack

Backend

FastAPI
Python
OpenAI API

Frontend

HTML / JavaScript
Web Speech API

Concepts

Streaming responses
Prompt engineering
Session-based memory
Resume grounding
🧩 Use Cases
Mock interview practice
Project explanation training
System design Q&A
Bilingual interview prep
⚠️ Notes
Use Chrome for best voice recognition
API Key is required
resume.json should not be too large (< ~2000 tokens)
🔮 Future Improvements
Real-time streaming voice (no stop required)
TTS (AI voice output)
Multi-user authentication
Persistent chat history (Redis / DB)
AI interviewer mode
🧠 Key Learnings
Prompt design strongly controls LLM behavior
Resume grounding reduces hallucination
Streaming improves user experience significantly
Voice UX requires latency optimization
👤 Author

Bruce Zhang
Backend / Distributed Systems / AI Engineer
Focus: LLM + Kubernetes + Observability + Data Systems

⭐ If you like this project

Give it a star ⭐


