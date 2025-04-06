from flask import Flask, request, jsonify
from TTS.api import TTS
import os

app = Flask(__name__)
tts = TTS("tts_models/vi/viettel/viettel_fastspeech2")  # Hoặc model bạn muốn

@app.route("/speak", methods=["POST"])
def speak():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "Missing text"}), 400
    path = "output.wav"
    tts.tts_to_file(text=text, file_path=path)
    return jsonify({"url": request.host_url + path})

@app.route("/output.wav")
def serve_audio():
    return app.send_static_file("output.wav")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
