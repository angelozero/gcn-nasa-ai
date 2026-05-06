import re
import json


def extract_json(text: str) -> dict:
    """Extrai o primeiro objeto JSON de uma string, ignorando markdown."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return {}
