# 🌊 Digi-Bayani: Typhoon & Flood Intelligence System

Digi-Bayani (Digital Hero) is an intelligent disaster response dashboard designed to classify social media posts (Tweets) in English, Filipino, and Taglish. By utilizing Natural Language Processing (NLP) and Knowledge Representation & Reasoning (KRR), the system prioritizes urgent reports to assist emergency responders in identifying genuine crises amidst real-time data noise.

## 🚀 Key Features

- **Multilingual Support**: Specifically trained to understand Philippine disaster context, including Taglish and code-switching.
- **Hybrid Intelligence**: Combines a Logistic Regression Machine Learning model with Rule-Based Reasoning to determine severity.
- **Real-Time Classification**: Instant feedback via a web-based dashboard (Flask/Streamlit).
- **High Recall**: Optimized with a 98% recall rate for disaster-related content to ensure no cry for help goes unnoticed.

## 🛠️ Technical Stack

- **Language**: Python 3.x
- **Machine Learning**: Scikit-learn (TF-IDF Vectorization, Logistic Regression)
- **Backend**: Flask (for Web API)
- **Frontend**: HTML5, CSS3 (Glassmorphism UI), Vanilla JavaScript
- **Alternative UI**: Streamlit (for rapid prototyping)

## 📂 Project Structure

```
Digi-Bayani/
├── flask_app.py            # Main Backend API (Flask)
├── app.py                  # Alternative Streamlit Interface
├── index.html              # Frontend Dashboard
├── styles.css              # Dashboard Styling
├── script.js               # Frontend Logic & API Integration
├── DT.ipynb                # Model Training & Evaluation Notebook
├── new_model.pkl           # Trained Logistic Regression Model
├── tfidf_vectorizer_new.pkl # Serialized TF-IDF Vectorizer
├── new_label_encoder.pkl   # Numerical Label to Text Decoder
└── tweet_examples.txt      # Curated list for Testing & Debugging
```

## 🧠 The Pipeline

- **Data**: Combined datasets from Typhoon Yolanda (2013) and Philippine Floods (2012).
- **Preprocessing**: Custom Regex cleaning to strip URLs, @mentions, hashtags, and punctuation.
- **ML Classification**: Predicts one of three categories:
  - 0: Disaster-Related
  - 1: Not Disaster-Related
  - 2: Uncertain / Needs Review
- **KRR Logic**: Applies severity rules (e.g., If the tweet contains "Rescue" or "Help", trigger a Severity 1 High-Priority alert).

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Digi-Bayani.git
   cd Digi-Bayani
   ```

2. **Install Dependencies**
   ```bash
   pip install flask flask-cors scikit-learn pandas numpy streamlit
   ```

3. **Run the System**

   You can run the system using either the Flask Backend or the Streamlit App:

   - **Option A: Flask Web Dashboard (Recommended)**
     - Start the server:
       ```bash
       python flask_app.py
       ```
     - Open `index.html` in your web browser.

   - **Option B: Streamlit Interface**
     ```bash
     streamlit run app.py
     ```

## 🧪 Testing & Debugging

The system includes a `test_model.py` script and a `tweet_examples.txt` file to verify performance.

| Input | Expected Label |
|-------|----------------|
| "Baha na naman sa Marikina, saklolo!" | Disaster-Related |
| "I love pizza #foodie" | Not Disaster-Related |
| "Stay safe everyone" | Uncertain / Needs Review |

## 👥 Group 1 - BSCS 3B

- Bulos, Mariabel M. – Model Creation & Training
- Ramos, Railey Mar M. – Website Development & API
- Rosario, Keanne Jericho M. – Documentation & Narrative Reports

## 📜 References

- **Dataset**: CrisisLex.org (CrisisLexT26)
- Specialized local data from Typhoon Yolanda and 2012 Floods.
