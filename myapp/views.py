import os
from myapp.emotion_detection_model import my_model_pipeline, load_my_model_from_huggingface
from flask import render_template, request

UPLOAD_FOLDER = './static/upload'

def index():
    
    return render_template('index.html')

def web_app():
    return render_template('web_app.html')

def emo_detection():

    if request.method == 'POST':
        f = request.files['image_name']
        filename = f.filename
        print(filename)
        # save our image in upload folder
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)
    # get prediction
        output = my_model_pipeline(path)
        print(output)
        # get the maximum value from the output
        if len(output) > 0:
            emotion = output[0]['label']
            probability = output[0]['score']

        

        return render_template('emotion.html', fileupload = True, emotion = emotion, probability=probability, image = filename)
    return render_template('emotion.html', fileupload = False)
