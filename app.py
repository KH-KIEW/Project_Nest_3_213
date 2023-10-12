from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        # Get the input text and target language from the form
        source_text = request.form['code']
        target_language = request.form['target_language']

        # Translate the text
        translated_text = translate_text(source_text, target_language)

        # Render the translation result
        return render_template('translation.html', source_text=source_text, translated_text=translated_text)

    return render_template('index.html')

def translate_text(text, target_language):
    from googletrans import Translator
    translator = Translator()
    translation = translator.translate(text, src='auto', dest=target_language)
    return translation.text

if __name__ == '__main__':
    app.run(debug=True)