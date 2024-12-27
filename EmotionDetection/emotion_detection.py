import requests
import json

'''
Execute emotion detection 
'''
def emotion_detector(text_to_analyze):
    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = myobj, headers = headers)

    if response.status_code == 400:
        emotions_none = {"anger":"None",
                         "disgust":"None",
                         "fear":"None",
                         "joy":"None",
                         "sadness":"None",
                         "dominant_emotion":"None"}
        return emotions_none

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Extraction of emotions from formatted response
    emotions_data = formatted_response["emotionPredictions"][0]["emotion"]

    # Find Max value key
    dominant_emotion = max(emotions_data, key = emotions_data.get)

    #add dominant emotion into emotions_data dictionary
    emotions_data['dominant_emotion'] = dominant_emotion
    
    return emotions_data
