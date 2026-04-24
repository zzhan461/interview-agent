import json
import uuid
from typing import Dict, List

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI()

# =========================
# Load Resume
# =========================
with open("resume.json", "r", encoding="utf-8") as f:
    RESUME = json.load(f)

def build_resume_text(resume: dict) -> str:
    return json.dumps(resume, indent=2)

RESUME_TEXT = build_resume_text(RESUME)

# =========================
# 🔥 双语强化 Prompt
# =========================
SYSTEM_PROMPT = f"""
You are a senior software engineer helping a candidate in a mock interview.

Candidate Resume:
{RESUME_TEXT}

--------------------------------
Core Tasks:
- Understand BOTH Chinese and English input
- Extract keywords
- Generate interview-ready answers grounded in the resume

--------------------------------
CRITICAL SAFETY RULES (MUST FOLLOW):

1. If you are NOT sure about a concept, question, or term:
   - DO NOT guess
   - DO NOT fabricate
   - DO NOT generate incorrect explanations

   Instead say:
   - English: "I’m not fully sure about this, but here’s what I understand..."
   - 中文: "这个问题我不太确定，我可以根据已有理解解释一下..."

2. If the question references something NOT in the resume:
   - DO NOT invent fake experience
   - You may:
     - explain concept generally
     - OR say you have not directly worked on it

3. If information is insufficient:
   - Ask a clarification question

--------------------------------
Language Rules:
- ALWAYS output BOTH English and Chinese
- Think in English for accuracy
- Chinese must be natural and correct

--------------------------------
Question Handling:

1. Technical Questions:
- Explain clearly
- Use real engineering intuition
- If unsure → explicitly say uncertainty

2. Project Questions:
- ONLY use provided resume
- No hallucinated projects

3. Follow-up Questions:
- Answer directly
- Add depth if confident

--------------------------------
STRICT OUTPUT FORMAT:

[Keywords]
- ...

[Answer - English]
...

[Answer - 中文]
...

--------------------------------
Style:
- concise
- practical
- honest > confident
"""

# =========================
# Session memory
# =========================
chat_sessions: Dict[str, List[dict]] = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/new-session")
def new_session():
    session_id = str(uuid.uuid4())
    chat_sessions[session_id] = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    return {"session_id": session_id}

@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    if req.session_id not in chat_sessions:
        chat_sessions[req.session_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    messages = chat_sessions[req.session_id]

    # 🔥 自动语言增强（关键）
    enhanced_input = f"""
User Input:
{req.message}

Understand Chinese + English correctly.
Respond in BOTH languages.
"""

    messages.append({
        "role": "user",
        "content": enhanced_input
    })

    # 控制长度
    if len(messages) > 24:
        chat_sessions[req.session_id] = [messages[0]] + messages[-22:]
        messages = chat_sessions[req.session_id]

    def generate():
        full_reply = ""

        stream = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            stream=True,
            temperature=0.3
        )

        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                full_reply += delta
                yield delta

        messages.append({
            "role": "assistant",
            "content": full_reply
        })

    return StreamingResponse(generate(), media_type="text/plain")

app.mount("/", StaticFiles(directory="static", html=True), name="static")