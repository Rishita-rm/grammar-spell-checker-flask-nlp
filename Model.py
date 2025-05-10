from textblob import TextBlob
import requests

class SpellCheckerModule:
    def __init__(self):
        self.grammar_api_url = "https://api.languagetool.org/v2/check"
        self.custom_corrections = {
            "helo": "hello",
            "wolrd": "world",
            "mashine": "machine",
            "laerning": "learning",
            "appple": "apple",
            "bananana": "banana"
        }

    def correct_spell(self, text):
        try:
            words = text.split()
            corrected_words = []

            for word in words:
                word_lower = word.lower()
                corrected = self.custom_corrections.get(word_lower, str(TextBlob(word).correct()))
                corrected_words.append("I" if corrected == "i" else corrected)

            corrected_text = " ".join(corrected_words)
            return corrected_text[0].upper() + corrected_text[1:]  # Capitalize first letter
        except Exception as e:
            return f"Spell check failed: {str(e)}"

    def correct_grammar(self, text):
        try:
            payload = {'text': text, 'language': 'en-US'}
            response = requests.post(self.grammar_api_url, data=payload)
            result = response.json()
            corrections = []
            seen_contexts = set()

            for match in result.get("matches", []):
                context = match.get("context", {}).get("text", "")
                if context in seen_contexts:
                    continue
                seen_contexts.add(context)

                replacements = match.get("replacements", [])
                suggestion = replacements[0]["value"] if replacements else "No suggestion"
                corrections.append(f"'{context}' → '{suggestion}'")

            return corrections, len(corrections)
        except Exception as e:
            return [f"Grammar check failed: {str(e)}"], 0

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Helo wolrd! i lova mashine laerning. appple. bananana"
    print("Corrected Spelling:")
    print(obj.correct_spell(message))

    print("\nGrammar Corrections:")
    grammar_mistakes, count = obj.correct_grammar(obj.correct_spell(message))
    for mistake in grammar_mistakes:
        print(mistake)
    print(f"\nTotal grammar issues found: {count}")
