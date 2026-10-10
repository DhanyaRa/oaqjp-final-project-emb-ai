# Final project

This project implements an emotion detection application using the Watson Emotion Detection service.

## Features
- Detects anger, disgust, fear, joy, and sadness in text.
- Identifies the dominant emotion.
- Provides a Flask web interface for submitting text.
- Handles empty input and service errors.
- Includes unit tests for the emotion detector.

## Files
- `EmotionDetection/emotion_detection.py` — emotion detection function.
- `EmotionDetection/__init__.py` — package import.
- `test_emotion_detection.py` — unit tests.
- `server.py` — Flask web application.
- `templates/index.html` — web interface.

## Run the application

```bash
python3 server.py
```

Open the application using the Skills Network preview for port 5000.
