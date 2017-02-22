import nltk
import string 
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

stopwords=['.','!',';',',','\'',':','-','_','?']
text="ASD@#AS...!    !!.. SAA  SDdsaa www!!:   "
tokens = nltk.word_tokenize(text)
print tokens
tokens = [i for i in tokens if i not in string.punctuation]
stems = stem_tokens(tokens, stemmer)
print stems
