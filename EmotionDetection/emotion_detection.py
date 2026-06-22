import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes input text using Watson NLP to determine emotion metrics.
    Handles blank inputs or invalid 400 requests by returning a blank dictionary layout.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Task 7 Error Handling: Fallback for blank inputs prior to network processing
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    
    # Task 7 Error Handling: Fallback layout on API error statuses
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    emotion_list = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    
    # Task 3 Formatting: Determine the highest ranking score value attribute
    dominant_emotion = max(emotion_list, key=emotion_list.get)
    emotion_list['dominant_emotion'] = dominant_emotion
    
    return emotion_list