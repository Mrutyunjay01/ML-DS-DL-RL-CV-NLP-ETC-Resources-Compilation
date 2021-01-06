# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 02:27:44 2020

@author: MRUTYUNJAY BISWAL
"""
import spacy
from nltk.tokenize import TweetTokenizer as TT


# tokenization
nlp = spacy.load('en')
text = 'Magna is a bitch'

# print the word tokens
print([str(token) for token in nlp(text)])

tweet= u"Snow White and the Seven Degrees #MakeAMovieCold@midnight:)"
tokenizer = TT()
print(tokenizer.tokenize(tweet))

# n-Grams
def n_grams(text, n):
    """
    takes tokens or text, returns a list of ngrams

    Parameters
    ----------
    text : A text or sequence.
    n : the value of n-gram model

    Returns
    -------
    n_gram tokens

    """
    return [text[i: i+n] for i in range(len(text)-n + 1)]

print(n_grams(tweet, 3))

# lemmatization in spacy
doc = nlp(u"He was running late.")
for token in doc:
    print(f"{token} -> {token.lemma_}")

# parts of speech tagging or POS tagging
doc1 = nlp(u"Marry slapped the green witch")
for token in doc1:
    print(f"{token} -> {token.pos_}")
    
# chunking or shallow parsing
# shallow parsing aims to derive higher order units composed of the grammatical
# atoms like noun, verbs, adjectives etc.
print("\nExample of shallow parsing...")
for token in doc1.noun_chunks:
    print(f"{token} -> {token.label_}")
        
    