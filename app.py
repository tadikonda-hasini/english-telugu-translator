from flask import Flask, render_template, request, jsonify
from translator import translate_text

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    text = data.get("text", "").strip()
    direction = data.get("direction", "en-te")

    if not text:
        return jsonify({"error": "Please enter some text."}), 400

    try:
        if direction == "en-te":
            source = "eng_Latn"
            target = "tel_Telu"
        else:
            source = "tel_Telu"
            target = "eng_Latn"

        translated_text = translate_text(text, source, target)

        return jsonify({
            "translation": translated_text
        })

    except Exception as e:
        return jsonify({
            "error": "Translation failed. Please try again."
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)