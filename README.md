# conversational-bot
A fast api based conversational bot that can be integrated with any RAG framework

# Run
```python
pip install -r requirements.txt
python main.py
```

# Usage
```curl
curl -X POST "http://localhost:8000/chat" \
-H "Authorization: Bearer your_bearer_token" \
-H "Content-Type: application/json" \
-d '{"user_id": "user123", "user_query": "Hello, how can I help you?"}'
````