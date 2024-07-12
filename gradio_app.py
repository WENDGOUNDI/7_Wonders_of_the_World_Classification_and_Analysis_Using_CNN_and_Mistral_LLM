import numpy as np
import gradio as gr
from predict_world_wonders_gradio import world_wonder_prediction_gradio
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import cv2
from dotenv import load_dotenv
import os

# take environment variables from .env.
load_dotenv()
# Retrevive mistral key from environment and define a model
mistral_key = os.getenv("MISTRAL_API_KEY")



def chatbot_mistral(world_wonder):

    """ This function takes as input the label predicted by the CNN model and provide further information such as
    the wonder's location, spoken language, currency, best time to visit, and climate."""

    # Define mistral client and model
    client = MistralClient(api_key=mistral_key)
    model = "mistral-small-latest"
    # Define our prompt to guide the llm
    my_prompt = f"""You are a smart assistant for a travel agency. Give us a brief description about {world_wonder}. 
                            Tell us in which country this place is, the spoken language of that country, the country's currency, when is the best time in the year to visit there, the climat.
                            Generate a json like response with the corresponding keys: description, language, location, currency, best time to visit, climat without curly brackets.

                            """
    messages = [
       ChatMessage(role="user", content=my_prompt)
   ]

    # Setting the chat (interaction with the chatbot)
    chat_response = client.chat(
       model=model,
       messages=messages,
   )
    llm_result = chat_response.choices[0].message.content

    # Filter the result
    final_result = list()
    for i in llm_result.split("\n"):
        cleaned_text = i.replace('"', '')
        if "description" in cleaned_text:
            final_text = cleaned_text.replace('description:', '')
            final_result.append(final_text)
        if "language" in cleaned_text:
            final_text = cleaned_text.replace('language:', '')
            final_result.append(final_text)
        if "location" in cleaned_text:
            final_text = cleaned_text.replace('location:', '')
            final_result.append(final_text)
        if "currency" in cleaned_text:
            final_text = cleaned_text.replace('currency:', '')
            final_result.append(final_text)
        if "best time to visit" in cleaned_text:
            final_text = cleaned_text.replace('best time to visit:', '')
            print(final_text)
            final_result.append(final_text)
        if "climat" in cleaned_text:
            final_text = cleaned_text.replace('climat:', '')
            final_result.append(final_text)

    return final_result[0], final_result[1], final_result[2], final_result[3], final_result[4], final_result[5]

def analyze_image(input_image):
    """ This function perform an image recognition to recognize the uploaded landmark."""
    # Resizing the image to 224x224
    resized_image = cv2.resize(input_image, (224, 224))
    # Reshape the image to (1, 224, 224, 3)
    reshaped_image = np.reshape(resized_image, (1, 224, 224, 3))
    pred_label = world_wonder_prediction_gradio(reshaped_image)
    llmanalysis = chatbot_mistral(pred_label)

    return llmanalysis

# Define our webapp image field as well as the text fields to display the llm responses
image = gr.Image()
description_field = gr.Textbox(label="Description")
language_field = gr.Textbox(label="Language")
location_field = gr.Textbox(label="Location")
currency_field = gr.Textbox(label="Currency")
best_time_to_visit_field = gr.Textbox(label="Best Time To Visit")
climat_field = gr.Textbox(label="Climat")

# Define webapp title and project description
title = "Wonders of the World Classification & Analysis via CNN and LLM"
project_description = (
    "Upload an image of one of the 7 world wonders, and our web app will identify it using a computer vision model. You will receive a brief description from Mistral, including the wonder's \
        location, spoken language, currency, best time to visit, and climate.")

if __name__ == "__main__":
    app_body = gr.Interface(fn=analyze_image,title=title, description=project_description, inputs=image, outputs=[description_field,
                                                                    language_field,
                                                                    location_field,
                                                                    currency_field,
                                                                    best_time_to_visit_field,
                                                                    climat_field])
                                                                
    app_body.launch()
