from flask import Flask, render_template, request, jsonify
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import string
import logging

# Download required NLTK packages
nltk.download('punkt')
nltk.download('wordnet')

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logs = []  # Store logs for display

# Load corpus
with open('chatbot.txt', 'r', encoding='utf-8') as file:
    corpus = file.read()

# Preprocess corpus into sentences
sent_tokens = nltk.sent_tokenize(corpus)
lemmatizer = nltk.WordNetLemmatizer()

def preprocess(text):
    """
    Preprocess user input by converting to lowercase,
    tokenizing, and lemmatizing.
    """
    tokens = nltk.word_tokenize(text.lower())
    return ' '.join([lemmatizer.lemmatize(word) for word in tokens if word.isalpha()])

def get_similarity_scores(user_input):
    """
    Calculate similarity scores between the user's input
    and the sentences in the corpus using TF-IDF.
    """
    user_input = preprocess(user_input)
    sent_tokens.append(user_input)  # Add user input to the corpus temporarily
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sent_tokens)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    sent_tokens.pop()  # Remove user input after calculating
    return similarity_scores[0]

def generate_response(user_input):
    """
    Generate chatbot response based on the highest similarity score.
    """
    similarity_scores = get_similarity_scores(user_input)
    max_index = np.argmax(similarity_scores)
    max_score = similarity_scores[max_index]

    # Log the query and scores
    logs.append({
        "user_input": user_input,
        "similarity_scores": similarity_scores.tolist(),
        "confidence": f"{(max_score * 100):.2f}%",
        "selected_response": sent_tokens[max_index] if max_score > 0.3 else "No close match"
    })

    # Select response based on confidence threshold
    if max_score > 0.3:
        return sent_tokens[max_index]
    else:
        return "I'm sorry! I couldn't find a relevant answer. Can you rephrase your question?"

@app.route('/')
def home():
    """Render the chatbot interface."""
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    """
    Handle user input and return the chatbot response as JSON.
    """
    try:
        user_input = request.json.get('message', '')
        if not user_input:
            return jsonify({'response': "Please enter a valid message!"}), 400
        response = generate_response(user_input)
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return jsonify({'response': "An error occurred. Please try again later."}), 500

@app.route('/logs')
def show_logs():
    """Render the logs interface."""
    return render_template('logs.html')

@app.route('/get_logs', methods=['GET'])
def get_logs():
    """
    Fetch the last 10 logs for display on the logs page.
    """
    return jsonify(logs[-10:])

if __name__ == '__main__':
    app.run(debug=True)
