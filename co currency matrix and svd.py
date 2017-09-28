#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:22:26 2017

@author: allen
"""

# use svd vector from co-occurence matrix and visualize corelation
import sys
import numpy as np
import matplotlib.pyplot as plt
axes = plt.gca()

from sklearn.feature_extraction.text import CountVectorizer
enc = sys.getdefaultencoding()
la = np.linalg

file = open("sample.txt", "r", encoding = enc)
read_File = file.read()

docs = read_File.split()

count_model = CountVectorizer(ngram_range=(1,1),min_df=0., max_df=1.0) # default unigram model
X = count_model.fit_transform(docs)
Xc = (X.T * X) # co-occurrence matrix
Xc.setdiag(0) # fill same word cooccurence to 0 => diagnol is all 0
U, s, vh = la.svd(Xc.todense(), full_matrices=False)
words = count_model.get_feature_names()
for i in range(len(words)):
    plt.text(U[i,0],U[i,1],words[i])