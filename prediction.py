import pickle
import os
import sys
import numpy as np
import operator
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
#from tensorflow.keras.utils import img_to_array,load_img
from keras.models import Sequential, load_model
from keras.preprocessing import image
from keras.preprocessing import image as image_utils
from keras.preprocessing import image
from keras import backend as K
import cv2

def img_prediction(test_image):
    K.clear_session()
    data = []
    img_path = test_image
    testing_img = cv2.imread(img_path)
    cv2.imwrite("..\AI_SAS\static\\detection.jpg", testing_img)
    model_path = 'vgg16_model.h5'
    model = load_model(model_path)
    test_image = load_img(img_path, target_size=(128, 128))
    test_image = img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image /= 255
    prediction = model.predict(test_image)
    max_confidence = np.max(prediction)
    print("max_confidence",max_confidence)
    
    # Check confidence threshold
    if max_confidence < 0.7:  # Adjust threshold as needed
        return "Invalid image, please select a valid image."
    else:
        lb = pickle.load(open('label_transform.pkl_vgg16', 'rb'))
        #print("lb",lb)
        prediction= lb.inverse_transform(prediction)[0]
        print("prediction", prediction)

        K.clear_session()
        return prediction

#img_prediction("apple1.JPG")