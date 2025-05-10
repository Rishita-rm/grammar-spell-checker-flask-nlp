from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spell', methods=['POST', 'GET'])
def spell():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        grammar_corrections, grammar_count = spell_checker_module.correct_grammar(
            corrected_text)
        return render_template('index.html',
                               corrected_text=corrected_text,
                               grammar_corrections=grammar_corrections,
                               grammar_count=grammar_count)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
