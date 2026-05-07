#1. Install NLTK
#NLTK (Natural Language Toolkit) is a Python library used for Natural Language Processing
#(NLP) tasks such as tokenization, stemming, tagging, and classification.
#Run the following command in the terminal or command prompt:
#pip install nltk
#2. Download NLTK Data
#After installation, download the required tokenizer package.
import nltk
nltk.download('punkt_tab')
#3. Tokenizing Text Data
#Tokenization means splitting text into smaller units such as sentences or words.
#Python Program
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
# Sample text
text = "Natural Language Processing is an interesting field. It deals with text and language."
# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)
# Word Tokenization
words = word_tokenize(text)
print("Words:", words)
