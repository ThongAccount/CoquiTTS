from flask import Flask, request, send_file
from TTS.api import TTS
import os

app = Flask(__name__)

tts = TTS(model_name="tts_models/vi/viettel/viettel-tts-3", progress_bar=False, gpu=False)

@app.route("/speak", methods=["POST"])
def speak():
    text = request.form.get("text")
    if not text:
        return {"error": "No text provided"}, 400

    output_path = "output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return send_file(output_path, mimetype="audio/wav", as_attachment=False)
