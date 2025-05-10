from textblob import TextBlob
import language_tool_python

class SpellCheckerModule:
    def __init__(self):
        self.grammar_check = language_tool_python.LanguageTool('en-US')

    def correct_spell(self, text):
        try:
            corrected_text = str(TextBlob(text).correct())
            return corrected_text
        except Exception as e:
            return f"Spell check failed: {str(e)}"

    def correct_grammar(self, text):
        try:
            matches = self.grammar_check.check(text)
            corrections = []
            for match in matches:
                context = match.context
                suggestion = ', '.join(match.replacements)
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
