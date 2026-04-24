<div align="center">

# Interview Voice Agent · 面试语音助手

Resume-grounded, bilingual (EN + 中文) mock interview copilot with browser voice input and streaming responses.

<p>
  <a href="#quickstart">Quickstart</a> ·
  <a href="#features">Features</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#api">API</a> ·
  <a href="#notes--troubleshooting">Notes</a>
</p>

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-Streaming-009688?logo=fastapi&logoColor=white">
  <img alt="Web Speech API" src="https://img.shields.io/badge/Web%20Speech-Voice%20Input-111827">
  <img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-Chat%20Completions-000000?logo=openai&logoColor=white">
</p>

</div>

---

## What this is

This project helps you practice mock interviews by generating interview-ready answers that are **grounded in your `resume.json`**, while supporting **text + voice input** and **streaming output** in the browser.

## Features

- 🎤 **Voice + Text**: Web Speech API recognition in the browser (Chrome recommended)
- 🧾 **Resume-grounded**: answers are anchored to `resume.json` to avoid made-up experience
- ⚡ **Streaming**: token streaming from FastAPI to UI
- 🧠 **Session memory**: `/new-session` + `/chat/stream`
- 🌍 **Bilingual output**: English answer + Chinese explanation (固定输出结构)

## Demo (local)

- Start the server, then open `http://127.0.0.1:8000`
- Type a question, or click the voice button to speak

## Architecture

```mermaid
flowchart TD
  UI[Browser UI\nText + Voice] -->|Web Speech API| ASR[Speech Recognition]
  UI -->|HTTP| API[FastAPI]
  API -->|load| RESUME[resume.json]
  API -->|prompt + resume grounding| LLM[OpenAI Chat Completions\n(streaming)]
  LLM -->|tokens| API -->|StreamingResponse| UI
```

## Quickstart

### Prerequisites

- Python 3.10+
- An OpenAI API key in `OPENAI_API_KEY`

### Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
```

### Configure API key

```bash
export OPENAI_API_KEY="your_api_key"
```

### Prepare `resume.json`

This file is loaded on startup and injected into the system prompt.

Example:

```json
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
```

### Run

```bash
uvicorn main:app --reload
```

Then open `http://127.0.0.1:8000`.

## How it works (files)

- `main.py`: loads `resume.json`, builds a bilingual system prompt, streams model tokens back to the browser
- `static/index.html`: minimal chat UI + voice recognition + optional TTS

## API

- `GET /new-session` → returns `{ "session_id": "..." }`
- `POST /chat/stream` → streams plain text tokens

Request body:

```json
{ "session_id": "...", "message": "..." }
```

## Output format (model)

<details>
<summary>Click to expand</summary>

```text
[Keywords]
- ...

[Answer - English]
...

[Answer - 中文]
...
```

</details>

## Notes & Troubleshooting

- **Voice not working**: use Chrome, allow microphone permissions, then reload.
- **Mixed Chinese/English recognition**: tweak `recog.lang` in `static/index.html` (e.g. `zh-CN` / `en-US`).
- **Prompt too long / slow**: keep `resume.json` concise (avoid large raw text blocks).
- **Missing API key**: ensure `OPENAI_API_KEY` is set in your shell environment.

## Roadmap

- Real-time voice streaming (no manual stop)
- Better UI/UX (chat bubbles, markdown rendering)
- Persistent chat history (Redis/DB)
- Multi-user auth + interviewer mode
