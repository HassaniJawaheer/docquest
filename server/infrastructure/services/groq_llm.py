import os
import requests
from dotenv import load_dotenv
from server.interfaces.services.llm import LLM

load_dotenv()

class GroqLLM(LLM):
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")
        self.url = os.getenv("GROQ_API_URL", "https://api.groq.com/openai/v1/chat/completions")

        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set in environment variables")

        # Generation parameters
        self.max_tokens = int(os.getenv("GENERATION_MAX_TOKENS", 512))
        self.temperature = float(os.getenv("GENERATION_TEMPERATURE", 0.7))
        self.top_p = float(os.getenv("GENERATION_TOP_P", 1.0))
        self.frequency_penalty = float(os.getenv("GENERATION_FREQUENCY_PENALTY", 0.0))
        self.presence_penalty = float(os.getenv("GENERATION_PRESENCE_PENALTY", 0.0))

    def generate_answer(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "frequency_penalty": self.frequency_penalty,
            "presence_penalty": self.presence_penalty
        }

        response = requests.post(self.url, headers=headers, json=payload)

        if not response.ok:
            print(f"Groq returned {response.status_code}: {response.text}")
        response.raise_for_status()

        content = response.json()["choices"][0]["message"]["content"]

        return content
