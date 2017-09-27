#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:02:48 2017

@author: allen
"""



import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def get_sim_count(vec1,vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    return len(intersection)
    
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def output(s1,s2):
    vector1 = text_to_vector(s1)
    vector2 = text_to_vector(s2)
    cosine = get_cosine(vector1, vector2)
    sim_count = get_sim_count(vector1,vector2)
    print('\n\nBetween:\n', s1, '\n&\n' , s2)
    print("Cosine: ", cosine)
    print("Pair count: ", sim_count)


if __name__ == "__main__":
    # sample input found on google
    input = """IBM cognitive computing|IBM \"cognitive\" computing is a revolution| 
    ibm cognitive computing|'IBM Cognitive Computing' is a revolution? | 
    IBM cognitive computing|IBM \"cognitive\" computing is a revolution|
    the cognitive computing is a revolution"""
    
    strAry = input.split('|')
    
    #loop and compare pair wise
    str1 = ''
    str2 = ''
    for i in range(0,len(strAry)):
        #(0,1) (2,3) ...
        if i % 2 != 1:
            str1 = strAry[i].strip()
        else:
            str2 = strAry[i].strip()
            output(str1,str2)

