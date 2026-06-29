from pprint import pprint

from app.services.gemini_service import GeminiService


gemini = GeminiService()


response = gemini.generate_json(
    """
Return ONLY JSON

{
    "name":"Chetan",
    "city":"Bangalore"
}
"""
)

pprint(response)