# EuroTranslate

This project is a Flask-based web application for translating text between various languages and summarizing the translated text if applicable. The application uses machine learning models for language detection, translation, and summarization.

## Features
- **Language Detection**: Automatically detects the language of the input text if the source language is set to `auto`.
- **Translation**: Translates text between multiple supported languages using Google Translator.
- **Summarization**: Summarizes the translated text if it contains more than two sentences using the `facebook/bart-large-cnn` model.

## Technologies Used
- **Backend**: Flask, Transformers (Hugging Face), Langdetect, Deep Translator
- **Frontend**: HTML, Bootstrap, JavaScript
- **Machine Learning**: Hugging Face's `facebook/bart-large-cnn` summarization model

## Setup Instructions

### Prerequisites
1. Python 3.8 or higher
2. pip (Python package manager)
3. GPU (optional, but recommended for faster summarization model inference)
4. Virtual environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **Dependencies include:**
   - Flask
   - Transformers
   - Langdetect
   - Deep Translator
   - torch (if not included with Transformers)

4. Ensure your system has the necessary machine learning model files by running the application once.

### Running the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter the text you want to translate in the input box.
2. Select the source language (or leave it as `Detect Language`).
3. Select the target language for translation.
4. Click on the "Translate" button.
5. View the translated text in the output box. The console will log the summarized text if applicable.

## File Structure
- **app.py**: Flask backend application.
- **templates/index.html**: Frontend HTML template.
- **static/**: Contains static assets (if needed).

## Customization
- **Language Map**: Add more languages in the `language_map` dictionary in `app.py` and JavaScript code.
- **Summarization Parameters**: Adjust the `max_length` and `min_length` parameters in the summarization pipeline for different summary lengths.

## Known Issues
1. **Performance**: The summarization model may run slowly on CPUs. Use a GPU for better performance.
2. **Language Detection**: The `langdetect` library may occasionally produce inaccurate results for very short or ambiguous text.

## Dependencies
List of libraries used (provided in `requirements.txt`):
- Flask
- langdetect
- deep-translator
- transformers
- torch

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Hugging Face for the BART summarization model
- Google Translator for translation functionality
- Bootstrap for frontend design

