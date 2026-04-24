# 🧠 Interview Voice Agent (AI Copilot for Mock Interviews)

A ChatGPT-like interview assistant with **resume grounding + bilingual support + voice input**, designed to help candidates generate **interview-ready answers in real time**.

---

## ✨ Features

- 🎤 **Voice Input (Chinese + English)**
  - Real-time speech recognition
  - Supports mixed-language queries

- 🧠 **Resume Injection**
  - Grounds answers using structured resume data
  - Prevents hallucinated experience
  - Generates realistic, personalized responses

- 🌍 **Bilingual Output**
  - Spoken English answer (interview-ready)
  - Chinese explanation for clarity

- ⚡ **Streaming Responses**
  - Token-level streaming like ChatGPT
  - Improved responsiveness and UX

- 💬 **Conversation Memory**
  - Maintains session-based context
  - Supports follow-up questions naturally

- 🔄 **Session Management**
  - Multi-session support
  - Clear/reset chat functionality

---

## 🏗️ Architecture

```text
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