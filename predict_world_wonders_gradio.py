
from tensorflow.keras.models import load_model  # TensorFlow is required for Keras to work
import numpy as np


def world_wonder_prediction_gradio(pred_image):
    # Load the model
    model = load_model("converted_keras/keras_model.h5", compile=False)

    # Load the labels
    class_names = open("converted_keras/labels.txt", "r").readlines()

    # Predicts the model
    prediction = model.predict(pred_image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    #print("Class:", class_name[2:], end="")
    #print("Confidence Score:", confidence_score)
    return class_name[2:]
