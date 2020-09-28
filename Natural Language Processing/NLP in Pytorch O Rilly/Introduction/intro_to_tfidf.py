# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 22:44:13 2020

@author: MRUTYUNJAY BISWAL
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

corpus = ['Time flies flies like an arrow.',
          'Fruit flies like a banana.']

one_hot_vectorizer = CountVectorizer(binary=True)
one_hot_vectors = one_hot_vectorizer.fit_transform(corpus).toarray()
print(one_hot_vectors)

plt.figure()
sns.heatmap(one_hot_vectors,
            annot=True,
            cbar=False)

tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(corpus)
print(tfidf.toarray())

plt.figure()
sns.heatmap(tfidf.todense(),
            annot=True,
            cbar=False)