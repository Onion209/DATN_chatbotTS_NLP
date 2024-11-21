# import pandas as pd
# import string

# # Dữ liệu mẫu cho câu hỏi và câu trả lời
# data = {
#     "user_a": ["Xin chào, bạn tên gì?", "Bạn đang làm gì?"],
#     "user_b": ["Tôi tên là Hành Lá.", "Tôi đang học lập trình."]
# }

# # Tạo DataFrame
# df = pd.DataFrame(data)
# df["user_a"] = df["user_a"].apply(lambda ele: ele.translate(str.maketrans('', '', string.punctuation)))
# print(df["user_a"])   
# # # Hiển thị 2 mẫu
# # for text in df['user_b'].values:
# #     for word in text.split():
# #         print(word)
# # arr = []
# # word = ["Tôi", "đang", "học", "lập", "trình."]
# # for word in word:
# #     if word not in ["lập", "trình."]:
# # #         arr.append(word)
# # # print(" ".join(arr))
# from torch.utils.data import Dataset, DataLoader

# class QADataset(Dataset):
#     def __init__(self, questions, answers):
#         self.questions = questions
#         self.answers = answers

#     def __len__(self):
#         return len(self.questions)

#     def __getitem__(self, idx):
#         question = self.questions[idx]
#         answer = self.answers[idx]
#         return question, answer

# # Giả sử bạn đã có các câu hỏi và câu trả lời đã được tiền xử lý
# questions = ["What is your name?", "How old are you?", "Where do you live?"]
# answers = ["My name is ChatGPT.", "I am a program, I don't have age.", "I live in the cloud."]

# # Tạo dataset
# qa_dataset = QADataset(questions, answers)

# # Tạo DataLoader
# qa_dataloader = DataLoader(qa_dataset, batch_size=2, shuffle=True)

# # Lặp qua các batch dữ liệu
# for batch in qa_dataloader:
#     questions_batch, answers_batch = batch
#     print("Questions:", questions_batch)
#     print("Answers:", answers_batch)
import keras_preprocessing
print(keras_preprocessing.__version__)
