
"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the emotion detector home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Analyze submitted text and return the detected emotions."""
    text_to_analyze = request.values.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    if result is None or result["dominant_emotion"] is None:
        return "Unable to detect emotion. Please try again.", 502

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
