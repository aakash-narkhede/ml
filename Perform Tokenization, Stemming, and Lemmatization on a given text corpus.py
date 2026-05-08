import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "The boys are playing games and running faster."
tokens = word_tokenize(text)
print("Tokens:", tokens)
ps = PorterStemmer()
stemmed = [ps.stem(word) for word in tokens]
print("Stemmed:", stemmed)
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word, pos='v') for word in tokens]
print("Lemmatized:", lemmatized)