import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
#import model

st.title('Detect objects anywhere everywhere')
st.write("Upload an image and see the magic!:zany_face:")

uploadedFile = st.file_uploader("UPLOAD IMAGE", type=['png','jpg','jpeg'])

if uploadedFile is not None:
    image = Image.open(uploadedFile)
    st.image(image, caption='Uplpoaded Image', use_column_width=True)
    #prediction = model.processImage(image)
    #prediction



