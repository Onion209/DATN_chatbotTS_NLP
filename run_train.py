from config import DATA_PATH, MODEL_PATH, HYPERPARAMETERS
from src.cleaning import load_data, sum_nan, usera_nan, fill_values
from src.dataset import QADataset
from src.models import define_model
from src.preprocessing import top10_rare_word, remove_emotion, remove_rare_word, preprocessing
from src.tokenization import tokenizer
from tensorflow.keras.utils import to_categorical  # Import to_categorical

# Load data
path = DATA_PATH['qa_short_type']
data = load_data(path)
# print(data.head(5))
data = preprocessing(data)
# print(data.head(5))

# Tokenization
input_data, output_data, tokenizer = tokenizer(data, max_len_input=20, max_len_output=20)
# print(input_data.shape, output_data.shape)

# Convert output_data to one-hot encoding
vocab_size = len(tokenizer.word_index) + 1
output_data_one_hot = to_categorical(output_data, num_classes=vocab_size)

# Define model
model = define_model(vocab_size, max_len_input=20, max_len_output=20, embedding_dim=100)

# Fit model with one-hot encoded output_data
model.fit([input_data, output_data], output_data_one_hot, batch_size=64, epochs=10, validation_split=0.2)

# Save model after training
model.save('attention_based_nmt_model.h5')
