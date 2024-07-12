# 7 World Wonders Classification Web App

## Project Overview
The "7 World Wonders Classification Web App" is an innovative platform designed to identify and provide detailed information about the seven wonders of the world through user-uploaded images. This project combines the power of computer vision and large language models to deliver an engaging and informative user experience.

## Dataset
This dataset from kaggle is a collection of the 7 wonders of the world. It was a campaign started in 2000 to choose Wonders of the World from a selection of 200 existing monuments.
It is large of 3846 images divided into 7 classes:
 - Venezuela Angel Falls
 - Taj Mahal
 - Stonehenge
 - Statue of Liberty
 - Chichen Itz
 - Christ the Redeemer
 - Pyramids of Giza
 - Eiffel Tower
 - Great Wall of China
 - Burj Khalifa
 - Roman Colosseum
 - Machu Pichu
#### Dataset Visualization
![dataset1](https://github.com/user-attachments/assets/eed02900-6dad-43df-8a25-709651f347a3)
![dataset2](https://github.com/user-attachments/assets/f2e4a4c9-b538-4e2c-a765-9955a7f3c44e)
![dataset3](https://github.com/user-attachments/assets/1d60bc86-b945-4a92-8eb9-d700119eb526)

## System Pipeline
![system_pipeline](https://github.com/user-attachments/assets/61378189-77f9-450b-b588-0613e87f9507)

## Key Features
 - Image Classification: Users can upload an image of any of the seven wonders of the world. The web app uses a state-of-the-art computer vision model to classify the image and identify the corresponding wonder.
 - LLM (Mistral) Analysis: Once the wonder is identified, a large language model, Mistral, generates brief description of the wonder and extras information such as location (country), country's spoken language, currency, best time to visit, and climate.

## Technical Implementation
- Frontend: The user interface allows users to upload images and view the classification results along with detailed descriptions and additional information.
- Backend:
   * Image Classification: Utilizes a pretrained computer vision model to accurately classify the uploaded images. The training is done through Teachable platform.
  * Description Generation: Integrates the Mistral language model to generate informative descriptions and relevant details about the wonder and its location.

## Use Cases
 - Educational Tool: The web app serves as an educational resource, offering users a fun and interactive way to learn about the seven wonders of the world.
 - Travel Planning: By providing detailed information about the best time to visit and the climate, the web app can assist users in planning their trips to these iconic destinations.
 - Cultural Awareness: The app promotes cultural awareness by sharing information about the language and currency of each wonder's location.

## Web App
![inference2](https://github.com/user-attachments/assets/85d00746-cc40-4208-9e90-f619daacc20a)
![inference3](https://github.com/user-attachments/assets/f15c8412-83dd-4459-94ef-ce448f92ba54)


## Reference
 - dataset link: https://www.kaggle.com/datasets/balabaskar/wonders-of-the-world-image-classification
