import streamlit as st
import sklearn
import pickle
import re
import string


# Define the clean_tweet_text function (must be available in the Streamlit app)
def clean_tweet_text(text):
    # 1a. Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    # 1b. Remove user mentions
    text = re.sub(r"@\w+", "", text)
    # 1c. Remove hashtags
    text = re.sub(r"#\w+", "", text)
    # 1d. Remove punctuation using string.punctuation and re.escape
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # 1e. Convert the text to lowercase
    text = text.lower()
    # 1f. Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Load the saved components
# Assuming these files are in the same directory as the Streamlit app script
try:
    with open("tfidf_vectorizer_new.pkl", "rb") as f:
        tfidf_vectorizer_new = pickle.load(f)
    with open("new_model.pkl", "rb") as f:
        new_model = pickle.load(f)
    with open("new_label_encoder.pkl", "rb") as f:
        new_label_encoder = pickle.load(f)
except FileNotFoundError:
    st.error(
        "Model components not found. Please ensure 'tfidf_vectorizer_new.pkl', 'new_model.pkl', and 'new_label_encoder.pkl' are in the same directory."
    )
    st.stop()  # Stop the app if files are not found


# Define the prediction function for Streamlit
def predict_new_informativeness(tweet_text):
    # Clean the input tweet text
    cleaned_text = clean_tweet_text(tweet_text)

    # Transform the cleaned text into TF-IDF features
    text_tfidf = tfidf_vectorizer_new.transform([cleaned_text])

    # Predict the class label using the trained model
    prediction = new_model.predict(text_tfidf)

    # Decode the numerical prediction back to the original categorical label
    decoded_label = new_label_encoder.inverse_transform(prediction)[0]

    return decoded_label


# Streamlit app layout
st.title("New Tweet Informativeness Classifier")
st.write(
    "Enter a tweet below to classify its informativeness regarding typhoons and floods."
)

user_input = st.text_area("Enter Tweet Text here:", "", height=150)

if st.button("Classify Tweet"):
    if user_input:
        result = predict_new_informativeness(user_input)
        st.success(f"Predicted Informativeness: {result}")
    else:
        st.warning("Please enter some text to classify.")
