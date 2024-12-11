from flask import Flask, render_template, request, jsonify
from langdetect import detect
from deep_translator import GoogleTranslator
from transformers import pipeline
import re

# Initialize Flask app
app = Flask(__name__)

# # Set Random Seed for Consistent Language Detection
# DetectorFactory.seed = 0

# # Load Summarization Model on GPU if available
# summarization_model = pipeline("summarization", model="facebook/bart-large-cnn", device=0)

# Language Map
language_map = {
    'english': 'en', 'spanish': 'es', 'french': 'fr', 'german': 'de',
    'italian': 'it', 'arabic': 'ar', 'chinese': 'zh-cn', 'japanese': 'ja',
    'portuguese': 'pt', 'russian': 'ru', 'hindi': 'hi', 'korean': 'ko'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        text = data.get("text", "")
        source_lang = data.get("source_lang", "auto")
        target_lang = data.get("target_lang", "en")

        # Detect language if source is auto
        if source_lang == "auto":
            detected_lang_code = detect(text)
            source_lang = detected_lang_code

        # Translate text
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)

        return jsonify({
            "translated_text": translated_text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)