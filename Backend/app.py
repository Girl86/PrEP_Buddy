from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return "PrEP AI Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    # System prompt (VERY IMPORTANT for health chatbot)
    system_prompt = """
    A safe, accurate HIV prevention assistant focused on PrEP.
    - Explain PrEP (oral and injectable) clearly
    - Be youth-friendly and non-judgmental
    - Do NOT provide dangerous medical instructions
    - Encourage users to consult healthcare providers when needed
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)