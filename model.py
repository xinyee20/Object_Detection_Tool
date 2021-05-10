import torch  
from PIL import Image
from base64 import decodebytes

def processImage(image):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5m')
    predictedImage = model(image)
    predictedImage.render()
    processedImage = Image.fromarray(predictedImage.imgs[0])
    return processedImage