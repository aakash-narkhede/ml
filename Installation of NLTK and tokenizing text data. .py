import nltk
nltk.download('punkt_tab')
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Natural Language Processing is an interesting field. It deals with text and language."

sentences = sent_tokenize(text)
print("Sentences:", sentences)

words = word_tokenize(text)
print("Words:", words)
