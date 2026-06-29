"""
Gemini Service

Wrapper around Google's Gemini API.
"""

import json

from google import genai

from app.config.settings import GOOGLE_API_KEY


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GOOGLE_API_KEY
        )

    def generate_json(
        self,
        prompt: str
    ) -> dict:

        response = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        text = response.text.strip()

        text = (
            text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(text)