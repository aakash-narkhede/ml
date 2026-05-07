import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
# Download required resources (run only once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
# Sample text
text = "The boys are playing games and running faster."
# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)
# Stemming
ps = PorterStemmer()
stemmed = [ps.stem(word) for word in tokens]
print("Stemmed:", stemmed)
# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word, pos='v') for word in tokens]
print("Lemmatized:", lemmatized)