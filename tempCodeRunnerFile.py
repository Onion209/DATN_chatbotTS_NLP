vocab_size = len(tokenizer.word_index) + 1
# model = define_model(vocab_size, max_len_input=20, max_len_output=20, embedding_dim=100)

# # Fit model
# model.fit([input_data, output_data], output_data, batch_size=64, epochs=10, validation_split=0.2)

# # Save model after training
# model.save('attention_based_nmt_model.h5')