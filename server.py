'''
Web application using flask library for the final project
'''

from flask import Flask, request, render_template, json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Final Project')

@app.route('/')
def home():
    '''
    Simple render homepage function
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    '''
    Method that queries to the emotion_detector service
    '''
    text = request.args.get('textToAnalyze')
    response = json.loads(emotion_detector(text))
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    output = f"""For the given statement, the system response is 'anger':
    {response['anger']}, 'disgust': {response['disgust']}, 'fear':
    {response['fear']}, 'joy': {response['joy']} and 'sadness':
    {response['sadness']}. The dominant emotion is {response['dominant_emotion']}"""
    return output

if __name__ == '__main__':
    app.run(debug=True)
