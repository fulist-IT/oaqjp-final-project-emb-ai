from EmotionDetection.emotion_detection import emotion_detector

import unittest

import json

class TestEmotionDetection(unittest.TestCase):

    def test_1(self):
        text = 'I am glad this happened'
        answer = json.loads(emotion_detector(text))
        dominant = answer['dominant_emotion']
        self.assertEqual(dominant,'joy')
    
    def test_2(self):
        text = 'I am really mad about this'
        answer = json.loads(emotion_detector(text))
        dominant = answer['dominant_emotion']
        self.assertEqual(dominant,'anger')

    def test_3(self):
        text = 'I feel disgusted just hearing about this'
        answer = json.loads(emotion_detector(text))
        dominant = answer['dominant_emotion']
        self.assertEqual(dominant,'disgust')

    def test_4(self):
        text = 'I am so sad about this'
        answer = json.loads(emotion_detector(text))
        dominant = answer['dominant_emotion']
        self.assertEqual(dominant,'sadness')

    def test_5(self):
        text = 'I am really afraid that this will happen'
        answer = json.loads(emotion_detector(text))
        dominant = answer['dominant_emotion']
        self.assertEqual(dominant,'fear')

unittest.main()
