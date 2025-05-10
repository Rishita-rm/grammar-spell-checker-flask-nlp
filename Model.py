from textblob import TextBlob
import requests

class SpellCheckerModule:
    def __init__(self):
        self.grammar_api_url = "https://api.languagetool.org/v2/check"

    def correct_spell(self, text):
        try:
            corrected_text = str(TextBlob(text).correct())
            return corrected_text
        except Exception as e:
            return f"Spell check failed: {str(e)}"

    def correct_grammar(self, text):
        try:
            payload = {
                'text': text,
                'language': 'en-US'
            }
            response = requests.post(self.grammar_api_url, data=payload)
            result = response.json()
            corrections = []
            for match in result.get("matches", []):
                context = match.get("context", {}).get("text", "")
                replacements = [r['value'] for r in match.get("replacements", [])]
                suggestion = ', '.join(replacements) if replacements else "No suggestion"
                corrections.append(f"'{context}' → '{suggestion}'")
            return corrections, len(corrections)
        except Exception as e:
            return [f"Grammar check failed: {str(e)}"], 0

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine learning. appple. bananana"
    print("Corrected Spelling:")
    print(obj.correct_spell(message))

    print("\nGrammar Corrections:")
    grammar_mistakes, count = obj.correct_grammar(message)
    for mistake in grammar_mistakes:
        print(mistake)
    print(f"\nTotal grammar issues found: {count}")
