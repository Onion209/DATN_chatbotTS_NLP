import numpy as np
import pandas as pd
from keras_preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def tokenizer(data, max_len_input, max_len_output):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data['user_a'])

    input_sequences = tokenizer.texts_to_sequences(data['user_a'])
    output_sequences = tokenizer.texts_to_sequences(data['user_b'])

    input_data = pad_sequences(input_sequences, maxlen=max_len_input, padding='post')
    output_data = pad_sequences(output_sequences, maxlen=max_len_output, padding='post')
    
    return input_data, output_data, tokenizer
