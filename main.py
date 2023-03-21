import os
from flask import Flask, render_template
from modes.Image.image import image
from modes.Audio.audio import audio
from modes.Text.text import text
from modes.Video.video import video

stega_path = 'input_media'

# stega_path = "C:\\Users\\USER\\Desktop"


UPLOAD_IMAGE_FOLDER = stega_path
IMAGE_CACHE_FOLDER = 'modes\\Image\\__pycache__'
UPLOAD_TEXT_FOLDER = stega_path
TEXT_CACHE_FOLDER = 'modes\\Text\\__pycache__'
UPLOAD_AUDIO_FOLDER = stega_path
AUDIO_CACHE_FOLDER = 'modes\\Audio\\__pycache__'
UPLOAD_VIDEO_FOLDER = stega_path
VIDEO_CACHE_FOLDER = 'modes\\Video\\__pycache__'


# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = "hello"
app.config['UPLOAD_IMAGE_FOLDER'] = UPLOAD_IMAGE_FOLDER
app.config['IMAGE_CACHE_FOLDER'] = IMAGE_CACHE_FOLDER
app.config['UPLOAD_TEXT_FOLDER'] = UPLOAD_TEXT_FOLDER
app.config['TEXT_CACHE_FOLDER'] = TEXT_CACHE_FOLDER
app.config['UPLOAD_AUDIO_FOLDER'] = UPLOAD_AUDIO_FOLDER
app.config['AUDIO_CACHE_FOLDER'] = AUDIO_CACHE_FOLDER
app.config['UPLOAD_VIDEO_FOLDER'] = UPLOAD_VIDEO_FOLDER
app.config['VIDEO_CACHE_FOLDER'] = VIDEO_CACHE_FOLDER
app.register_blueprint(image, url_prefix="/image")
app.register_blueprint(audio, url_prefix="/audio")
app.register_blueprint(text, url_prefix="/text")
app.register_blueprint(video, url_prefix="/video")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)