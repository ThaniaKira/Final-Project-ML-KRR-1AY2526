import pickle
import re
import string

def clean_tweet_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Load model components
with open('tfidf_vectorizer_new.pkl', 'rb') as f:
    tfidf = pickle.load(f)
with open('new_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('new_label_encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

print('Available label classes:', encoder.classes_)
print('Number of classes:', len(encoder.classes_))
print('-' * 60)

# Test with different tweets
test_tweets = [
    'Typhoon approaching Manila with heavy rainfall',
    'I love pizza and ice cream',
    'Heavy rainfall expected in 3 hours',
    'Good morning everyone!',
    'Flood warning issued for northern provinces',
    'Just watching Netflix'
]

for tweet in test_tweets:
    cleaned = clean_tweet_text(tweet)
    features = tfidf.transform([cleaned])
    pred = model.predict(features)
    label = encoder.inverse_transform(pred)[0]
    print(f'Tweet: "{tweet}"')
    print(f'Cleaned: "{cleaned}"')
    print(f'Prediction: {label}')
    print('-' * 60)
