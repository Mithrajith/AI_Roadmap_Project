from fastapi import FastAPI
import ollama

app =  FastAPI()

@app.get("/")
def home():
    return {"Message":"This is the Fastapi Backend"}


@app.post("/printname/{name}")
def printname(name):
    return {f"Hi user, {name}"}


@app.post("/chat/{ollama_chat}")
def chat(ollama_chat):
    ChatResponse = ollama.chat(
    model='llama3.2:latest',
    messages=[
        {
        'role': 'user',
        'content': ollama_chat,
        },
    ],
    )
    return {"Response":ChatResponse.message.content}