import requests
import json

def emotion_detector(text_to_analyze: str):

    URL: str = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS: dict =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT: dict = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(
        url=URL,
        headers=HEADERS,
        json=INPUT
    )

    # Returning the response form the analysis and parse to dict
    emotions_dict = json.loads(response.text)   
    emotions = emotions_dict['emotionPredictions'][0]['emotion']

    # Finding the dominant emotion
    highest_emotion = dict([max(emotions.items(), key=lambda x: x[1])]) 
    emotions['dominant_emotion'] = list(highest_emotion.keys())[0]

    return emotions