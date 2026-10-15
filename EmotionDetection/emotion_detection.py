import requests

import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 400:
        answer = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        return json.dumps(answer, indent=0)

    json_response = json.loads(response.text)
    anger_score = float(json_response['emotionPredictions'][0]['emotion']['anger'])
    disgust_score = float(json_response['emotionPredictions'][0]['emotion']['disgust'])
    fear_score = float(json_response['emotionPredictions'][0]['emotion']['fear'])
    joy_score = float(json_response['emotionPredictions'][0]['emotion']['joy'])
    sadness_score = float(json_response['emotionPredictions'][0]['emotion']['sadness'])

    answer = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
        }
    dominant_emotion = 'anger'

    for emotion in answer:  
        if (answer[emotion] > answer[dominant_emotion]):
           dominant_emotion = emotion
            
    answer['dominant_emotion'] = dominant_emotion
    
    return json.dumps(answer, indent=0)
