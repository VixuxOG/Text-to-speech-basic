from flask import Flask, render_template, request, send_file
import pyttsx3
import os

app = Flask(__name__)

def text_to_speech(text, filename="output.mp3"):  # Save to MP3 for browser compatibility
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    engine.stop()
    return filename

@app.route('/', methods=['GET', 'POST'])
def index():
    audio_file = None
    if request.method == 'POST':
        text_to_speak = request.form['text']
        if text_to_speak:
            audio_file_path = text_to_speech(text_to_speak, "static/output.mp3") # Save in 'static' folder
            audio_file = "output.mp3" # Relative path for HTML

    return render_template('index.html', audio_file=audio_file)

@app.route('/static/<filename>') # Route to serve static files (like audio)
def serve_static(filename):
    return send_file(os.path.join('static', filename))

if __name__ == '__main__':
    # Create a 'static' folder if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True) # debug=True for development