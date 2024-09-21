import tensorflow as tf
import pickle
import gradio as gr
import numpy as np
import json


with open('tokenizer.json') as file:
    tokenizer_data = file.read()
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_data)

         
def Infernce_Pipe(text,max_length = 100):
    model = tf.keras.models.load_model("LSTM_senti.h5")   

    sequences = tokenizer.texts_to_sequences([text])
    
    padded = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')
   
    pred = model.predict(padded)
    predicted_index = np.argmax(pred)
    # Define the label mapping
    labels = ['Negative', 'Neutral', 'Positive']

    # Map index to label
    predicted_label = labels[predicted_index]

    return predicted_label

interface = gr.Interface(
                            fn=Infernce_Pipe,  
                            inputs=gr.Textbox(placeholder="Enter text here..."),
                            outputs=gr.Text(label="Prediction"),
                            title="Sentiment Analysis on Customer Review",
                            description="Enter a review to get its sentiment classification (Negative, Neutral, Positive)."
                        )

interface.launch(share=True)

