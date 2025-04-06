from flask import Flask, request, jsonify
from TTS.api import TTS
import os

app = Flask(__name__)
tts = TTS(model_name="tts_models/vi/viet_tts_fpt", progress_bar=False, gpu=False)

@app.route("/speak", methods=["POST"])
def speak():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    out_path = "static/output.wav"
    tts.tts_to_file(text=text, file_path=out_path)

    return jsonify({"url": request.host_url + out_path})

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
