import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


import numpy as np
from textblob import TextBlob
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.preprocessing import image

model = MobileNetV2(weights="imagenet")

print("=========================================")
print("        AI RECOGNITION SYSTEM")
print("=========================================")
print("1. Image Recognition")
print("2. Text Sentiment Recognition")

choice = input("\nEnter your choice (1 or 2): ")

if choice == "1":

    img_path = input("\nEnter image filename (example: cat.jpg): ")

    try:
     
        img = image.load_img(img_path, target_size=(224, 224))

      
        img_array = image.img_to_array(img)

      
        img_array = np.expand_dims(img_array, axis=0)

 
        img_array = preprocess_input(img_array)

    
        predictions = model.predict(img_array)

     
        results = decode_predictions(predictions, top=3)[0]

        print("\n========== IMAGE RECOGNITION RESULT ==========")

        for i, result in enumerate(results, start=1):
            print(f"{i}. {result[1]} --> {result[2]*100:.2f}%")

    except FileNotFoundError:
        print("Image not found. Please check the filename.")

elif choice == "2":

    text = input("\nEnter a sentence: ")

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"

    elif polarity < 0:
        sentiment = "Negative 😞"

    else:
        sentiment = "Neutral 😐"

    print("\n========== TEXT RECOGNITION RESULT ==========")
    print("Text:", text)
    print("Sentiment:", sentiment)
    print("Polarity Score:", round(polarity, 2))


else:
    print("Invalid choice!")

print("\n=========================================")
print("Thank you for using the AI Recognition System!")
print("=========================================")