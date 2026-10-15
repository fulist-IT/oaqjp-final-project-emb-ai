
from flask import Flask, request, render_template, json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Final Project')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    text = request.args.get('textToAnalyze')
    response = json.loads(emotion_detector(text))

    output = f"""For the given statement, the system response is 'anger':
    {response['anger']}, 'disgust': {response['disgust']}, 'fear':
    {response['fear']}, 'joy': {response['joy']} and 'sadness':
    {response['sadness']}. The dominant emotion is {response['dominant_emotion']}"""
    return output


if __name__ == '__main__':
    app.run(debug=True)
