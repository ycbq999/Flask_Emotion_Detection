import requests
import time

API_URL = "https://api-inference.huggingface.co/models/ycbq999/facial_emotions_image_detection"
headers = {"Authorization": "Bearer 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"}


# image_path = '/workspaces/Flask_Emotion_Detection/Images/Girl_Scared2.jpg'


# we have to give the model some time to load this is the drawback of using the free version of huggingface or not using advanced web frameworks like django
def load_my_model_from_huggingface():
    response = requests.get(API_URL, headers=headers)
    
# query the model and return the output
def my_model_pipeline(filename):
    
    with open(filename, "rb") as f:
        data = f.read()
    print('loading model...')
    response = requests.post(API_URL, headers=headers, data=data)
    time.sleep(8)
    print('model loaded')    
    print('processing image...')
    time.sleep(6)
    return response.json()


# output = my_model_pipeline(image_path)

# print(output)