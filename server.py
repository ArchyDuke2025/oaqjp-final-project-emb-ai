'''
Execute Emotion Detection server for extract and show dominant
emotion.
'''
# Import Flask, render_template, request from the flask pramework package
# Import the emotion_detector function from the package created
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    sent_detector function for sent text and extract emotions
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # get the dominant emotion value
    dominant_emotion = response['dominant_emotion']

    # delete dominant_emotion key from response
    del response['dominant_emotion'] 

    # format response
    formatted_response = ", ".join(f"'{clave}': {valor}" for clave, valor in response.items())

    return f'For the given statement, the system response is {formatted_response}. The dominant emotion is <b>{dominant_emotion}</b>.'

@app.route("/")
def render_index_page():
    '''
    render_index_page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
