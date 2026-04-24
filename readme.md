# Interview Voice Agent

Resume-grounded, bilingual (EN + 中文) mock interview copilot with browser voice input and streaming responses.

## Highlights

- Voice input via Web Speech API (works best on Chrome)
- Resume grounding from `resume.json` (reduces hallucinated experience)
- Streaming responses (ChatGPT-like)
- Session memory (`/new-session` + `/chat/stream`)
- Bilingual output format: English answer + Chinese explanation

## Demo

- Open `http://127.0.0.1:8000` after starting the server
- Type a question or click the voice button to speak

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

## How it works

- Backend: `main.py` loads `resume.json`, builds a bilingual system prompt, and streams model tokens back to the browser.
- Frontend: `static/index.html` provides a minimal chat UI + voice recognition + optional TTS.

## API

- `GET /new-session` → returns `{ "session_id": "..." }`
- `POST /chat/stream` → streams plain text tokens

Request body:

```json
{ "session_id": "...", "message": "..." }
```

## Output format (model)

```text
[Keywords]
- ...

[Answer - English]
...

[Answer - 中文]
...
```

## Notes

- Chrome has the most reliable Web Speech support; ensure mic permissions are granted.
- If you want better mixed-language recognition, adjust `recog.lang` in `static/index.html`.
- Keep `resume.json` reasonably sized to avoid prompt bloat.

## Roadmap

- Real-time voice streaming (no manual stop)
- Better UI/UX (chat bubbles, markdown rendering)
- Persistent chat history (Redis/DB)
- Multi-user auth + interview mode
