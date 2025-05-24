# Do not forget to install the libs fastapi and openai.

from fastapi import FastAPI, Request
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/")
async def health():
    return {"status": "ok"}

@app.post("/agent")
async def run_agent(request: Request):
    body = await request.json()
    user_input = body.get("text", "")

    prompt = f"Summarize this: {user_input}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=150
        )
        output = response['choices'][0]['message']['content'].strip()
        return {"result": output}

    except Exception as e:
        return {"error": str(e)}
 