import pandas as pd
from collections import Counter
import string
EMOTION = { 
    u":-3":"Happy face smiley",
    u":3":"Happy face smiley",
    u":->":"Happy face smiley",
    u":>":"Happy face smiley",
    u":))":"Happy face smiley",
    u":)))":"Happy face smiley",
    u":))))":"Happy face smiley",
    u":'<":"Happy face smiley",
    u":)":"Happy face smiley",
    u":(":"Happy face smiley",
    u":((":"Happy face smiley",
    u":‑D":"Laughing, big grin or laugh with glasses",
    u":D":"Laughing, big grin or laugh with glasses",
    u"XD":"Laughing, big grin or laugh with glasses",
    u"=D":"Laughing, big grin or laugh with glasses",
    u":‑c":"Frown, sad, andry or pouting",
    u":c":"Frown, sad, andry or pouting",
    u":‑<":"Frown, sad, andry or pouting",
    u":<":"Frown, sad, andry or pouting",
    u":@":"Frown, sad, andry or pouting",
    u"D:":"Sadness",
    u":O":"Surprise",
    u":o":"Surprise",
}
# Get top 10 rare word

def remove_emotion(text):
    arr = []
    for word in text.split():
        if word not in EMOTION.keys():
            arr.append(word)
    return " ".join(arr)

def remove_rare_word(text, top_words):
    arr = []
    for word in text.split():
        if word not in top_words:
            arr.append(word)
    return " ".join(arr)

def top10_rare_word(data):
    count = Counter()
    for text in data['user_b'].values:
        for word in text.split():
            count[word] += 1
    top_words = [word for word, _ in count.most_common()[-10:]]
    return top_words

def preprocessing(data):
    # Remove punctuation
    data["user_a"] = data["user_a"].apply(lambda ele: str(ele) if not isinstance(ele, str) else ele)
    data["user_b"] = data["user_b"].apply(lambda ele: str(ele) if not isinstance(ele, str) else ele)
    data["user_a"] = data["user_a"].apply(lambda ele: ele.translate(str.maketrans('', '', string.punctuation)))
    data["user_b"] = data["user_b"].apply(lambda ele: ele.translate(str.maketrans('', '', string.punctuation)))
    
    # Remove emotion
    data["user_a"] = data["user_a"].apply(lambda ele: remove_emotion(ele))
    data["user_b"] = data["user_b"].apply(lambda ele: remove_emotion(ele))
    
    # Remove rare word
    top_words = top10_rare_word(data)
    data["user_a"] = data["user_a"].apply(lambda ele: remove_rare_word(ele, top_words))
    data["user_b"] = data["user_b"].apply(lambda ele: remove_rare_word(ele, top_words))
    
    # Add start and end to user_b
    data['user_b'] = data['user_b'].apply(lambda ele: 'START ' + ele + ' END')
    
    # Convert to lower
    data['user_a'] = data['user_a'].apply(lambda ele: ele.lower())
    data['user_b'] = data['user_b'].apply(lambda ele: ele.lower())
    
    return data



def prepare_data():
    pass


