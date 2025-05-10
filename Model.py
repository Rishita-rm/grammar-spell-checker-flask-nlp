from textblob import TextBlob
from gingerit.gingerit import GingerIt

class SpellCheckerModule:
    def __init__(self):
        self.grammar_check = GingerIt()

    def correct_spell(self, text):
        try:
            corrected_text = str(TextBlob(text).correct())
            return corrected_text
        except Exception as e:
            return f"Spell check failed: {str(e)}"

    def correct_grammar(self, text):
        try:
            matches = self.grammar_check.parse(text)
            corrections = []
            for error in matches.get('corrections', []):
                original = error.get('text', '')
                suggestion = error.get('correct', '')
                corrections.append(f"'{original}' → '{suggestion}'")
            return corrections, len(corrections)
        except Exception as e:
            return [f"Grammar check failed: {str(e)}"], 0
