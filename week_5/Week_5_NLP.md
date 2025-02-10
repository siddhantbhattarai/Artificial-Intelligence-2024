### **Exercise 1: Answer the quiz available via Canvas.**
- This exercise requires you to log in to Canvas and complete the quiz provided there.

---

### **Exercise 2: Install NLTK library and its dependencies.**
- To install the NLTK library, run the following command in your terminal or command prompt:
  ```bash
  pip install nltk
  ```

---

### **Exercise 3: Install scikit-learn library.**
- To install the scikit-learn library, run the following command in your terminal or command prompt:
  ```bash
  pip install scikit-learn
  ```

---

### **Exercise 4: Initialize the work with the provided script.**
- Run the following Python script to initialize the NLTK library and download necessary packages:
  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  nltk.download('wordnet')

  from nltk.corpus import stopwords
  from nltk.tokenize import word_tokenize
  import string

  # Sample text
  text = "This is a simple example of text preprocessing. It involves cleaning and organizing raw text data into a format suitable for analysis."

  print("Original Text: ")
  print(text)
  ```

---

### **Exercise 5: Convert the text to lowercase.**
- Use the `.lower()` method to convert the text to lowercase:
  ```python
  # Convert to lowercase
  text = text.lower()

  print("Lower case Text: ")
  print(text)
  ```

---

### **Exercise 6: Remove punctuation.**
- Use the `translate` method to remove punctuation:
  ```python
  # Remove punctuation
  text = text.translate(str.maketrans('', '', string.punctuation))

  print("Removed punctuation: ")
  print(text)
  ```

---

### **Exercise 7: Tokenize the sentence.**
- Use the `word_tokenize` tool to tokenize the text:
  ```python
  # Tokenization
  tokens = word_tokenize(text)
  print("All tokens: ")
  print(tokens)
  ```

---

### **Exercise 8: Remove stop words.**
- Use the `stopwords` corpus to remove stop words:
  ```python
  # Removing stopwords
  stop_words = set(stopwords.words('english'))
  filtered_tokens = [word for word in tokens if word not in stop_words]

  print("\nAfter Text Preprocessing: ")
  print(filtered_tokens)
  ```

---

### **Exercise 9: Repeat exercises 5-9 with 3 different sentences.**
- Choose 3 different sentences and repeat the preprocessing steps (lowercase, remove punctuation, tokenize, and remove stop words). For example:
  ```python
  # Example 1
  text1 = "Natural Language Processing is a fascinating field of study."
  # Repeat steps 5-8 for text1

  # Example 2
  text2 = "Machine learning algorithms are used to analyze data."
  # Repeat steps 5-8 for text2

  # Example 3
  text3 = "Text summarization helps in reducing long documents."
  # Repeat steps 5-8 for text3
  ```

---

### **Exercise 10: Create a text file and read it using Python.**
- Create a text file named `example.txt` with a paragraph of your choice. Then, read the file using Python:
  ```python
  # Open and read the text file
  with open('example.txt', 'r') as file:
      text = file.read()

  print("Text from file: ")
  print(text)
  ```

---

### **Exercise 11: Apply preprocessing steps to the text from the file.**
- Apply the preprocessing steps (lowercase, remove punctuation, tokenize, and remove stop words) to the text read from the file:
  ```python
  # Convert to lowercase
  text = text.lower()

  # Remove punctuation
  text = text.translate(str.maketrans('', '', string.punctuation))

  # Tokenize
  tokens = word_tokenize(text)

  # Remove stopwords
  stop_words = set(stopwords.words('english'))
  filtered_tokens = [word for word in tokens if word not in stop_words]

  print("\nPreprocessed Text from File: ")
  print(filtered_tokens)
  ```

---

### **Exercise 12: Use the Lemmatizer on a list of words.**
- Use the `WordNetLemmatizer` to lemmatize a list of words:
  ```python
  from nltk.stem import WordNetLemmatizer

  lemmatizer = WordNetLemmatizer()

  words = ['cats', 'cacti', 'geese', 'rocks', 'python', 'better']
  for word in words:
      print(f"Word: {word}, Lemma: {lemmatizer.lemmatize(word)}")
  ```

---

### **Exercise 13: Apply the Lemmatizer to the text file.**
- Apply the `WordNetLemmatizer` to the preprocessed tokens from the text file:
  ```python
  lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
  print("\nLemmatized Tokens: ")
  print(lemmatized_tokens)
  ```

---

### **Exercise 14: Perform sentence segmentation.**
- Use the `sent_tokenize` tool to segment a text into sentences:
  ```python
  from nltk import sent_tokenize

  text = "Hello! This is an example of sentence segmentation. It demonstrates how sentence segmentation works using NLTK. Hope you find it helpful."

  sentences = sent_tokenize(text)
  for sentence in sentences:
      print(sentence)
  ```

---

### **Exercise 15: Develop a text summarization script.**
- Create a script to summarize a text file into 3 sentences:
  ```python
  from nltk.tokenize import word_tokenize, sent_tokenize
  from nltk.corpus import stopwords
  from collections import defaultdict

  # Read the text file
  with open('example.txt', 'r') as file:
      text = file.read()

  # Tokenize sentences and words
  sentences = sent_tokenize(text)
  words = word_tokenize(text.lower())

  # Remove stopwords
  stop_words = set(stopwords.words('english'))
  filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

  # Calculate word frequencies
  word_frequencies = defaultdict(int)
  for word in filtered_words:
      word_frequencies[word] += 1

  # Calculate sentence scores
  sentence_scores = defaultdict(int)
  for sentence in sentences:
      for word in word_tokenize(sentence.lower()):
          if word in word_frequencies:
              sentence_scores[sentence] += word_frequencies[word]

  # Select top 3 sentences with the highest scores
  sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
  summary = ' '.join(sorted_sentences[:3])

  print("\nSummary: ")
  print(summary)
  ```

---

### **END OF SOLUTIONS**

Make sure to upload your notebook with the solutions to your ePortfolio as instructed.
