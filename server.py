"""
Flask server for Emotion Detection application.
This module provides a web interface for analyzing emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the main page of the application.

    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Handle emotion detection requests.

    Analyzes the text provided in the request and returns
    emotion scores and the dominant emotion. Returns an error
    message if the text is invalid.

    Returns:
        str: Formatted response with emotion analysis or error message
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (error case)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
