import requests
import time

API_URL = "https://api-inference.huggingface.co/models/ycbq999/facial_emotions_image_detection"
headers = {"Authorization": "Bearer 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"}


image_path = '/workspaces/Flask_Emotion_Detection/Images/Girl_Scared2.jpg'

# def read_image(image_path):
#     with open(image_path, 'rb') as f:
#         return f.read()
# image = read_image(image_path)

def query(filename):
    
    with open(filename, "rb") as f:
        data = f.read()
    print('loading model...')
    response = requests.post(API_URL, headers=headers, data=data)
    time.sleep(3)
    print('model loaded')    
    print('processing image...')
    time.sleep(3)
    return response.json()

output = query(image_path)

print(output)