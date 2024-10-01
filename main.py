from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Set your Bearer token here
BEARER_TOKEN = "your_bearer_token"
security = HTTPBearer()

# In-memory storage for user contexts (for demonstration purposes only)
user_contexts = {}

class Message(BaseModel):
    user_id: str
    user_query: str

def verify_bearer_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != BEARER_TOKEN:
        raise HTTPException(status_code=403, detail="Access forbidden: Invalid token")

@app.post("/chat")
async def chat(message: Message, credentials: HTTPAuthorizationCredentials = Depends(verify_bearer_token)):
    # Retrieve or initialize the context for the user
    context = user_contexts.get(message.user_id, [])
    
    # Simulate a response using the context (you can replace this with your RAG logic)
    response = f"Echo: {message.user_query}. Previous context: {context}"
    
    # Update the context with the new message
    context.append(message.user_query)
    user_contexts[message.user_id] = context  # Store the updated context
    
    return {"response": response, "context": context}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
