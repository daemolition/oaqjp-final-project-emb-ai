import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector():
    
    if request.method == "POST":
        
        text_to_analyze = request.args.get('textToAnalyze')        

        URL: str = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
        HEADERS: dict =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        INPUT: dict = { "raw_document": { "text": text_to_analyze } }
        
        response = requests.post(
            url=URL,
            headers=HEADERS,
            json=INPUT
        )
        
        print(response.status_code)
    
        # Returning the response form the analysis and parse to dict
        emotions_dict = json.loads(response.text)   
        emotions = emotions_dict['emotionPredictions'][0]['emotion']

        # Finding the dominant emotion
        highest_emotion = dict([max(emotions.items(), key=lambda x: x[1])]) 
        emotions['dominant_emotion'] = list(highest_emotion.keys())[0]

        print(emotions)

        return render_template("index.html", id=response.text)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9000)    