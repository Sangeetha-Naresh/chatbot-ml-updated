# The preprocessing is done in a Python file.
# performing Stemming operation and creating Bag of Words.

# import all the libraries required to preprocess our data.
# Start by importing nltk. NLTK is also known as the Natural Language Toolkit. 
# It isthe Python library used for preprocessing text data. 
# It has methods for cleaning the data and removing repetitive words.

import nltk
# download required NLTK data (punkt, wordnet).

# on some system if you encounter an error downloading nltk,
# in that case you can consider to modify the SSL context in Python to bypass SSL certificate verification.

nltk.download('punkt') #  for tokenizing text into sentences
nltk.download('wordnet') # a lexical database for English

# from NLTK we’ll import the PorterStemmer() class which  is responsible to give the stem words

# stemming -> reduces words to root words : cooks, cooking, cooked  -> cook
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

# reading and processing JSON data.
import json

# converts lists,dictionaries, and other objectt into a byte stream .
import pickle

# training dataset is numpy arrays
import numpy as np
import random


# to load our data.
train_data_file = open('./static/assets/chatbot_corpus/intents.json').read()
intents = json.loads(train_data_file)

words=[] 
classes = [] 
pattern_word_tags_list = [] 

# symbols should be avoided for text preprocessing
ignore_symbols = ['?', '!',',','.', "'s"]


# Define a function to get the stem word from the list of words.
def get_stem_words(words, ignore_symbols):
    stem_words = []
    for word in words:
        if word not in ignore_symbols:
            w = stemmer.stem(word.lower())
            stem_words.append(w)
    return stem_words


# chatbot corpus that is set of words that can be expected from user as input. 
def bot_corpus(words, classes, pattern_word_tags_list, ignore_symbols):

# To create a corpus, we first have to extract these words from intents.json. 
# We are using a for loop to iterate through each intent or tag
    
    for intent in intents['intents']:

        # Add all patterns and tags to a list
        for pattern in intent['patterns']:            
            pattern_word = nltk.word_tokenize(pattern)            
            words.extend(pattern_word)                        
            pattern_word_tags_list.append((pattern_word, intent['tag']))
              
    
        # Add all tags to the classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            
    stem_words = get_stem_words(words, ignore_symbols) 
    stem_words = sorted(list(set(stem_words)))
    classes = sorted(list(set(classes)))

    return stem_words, classes, pattern_word_tags_list

stem_words, tag_classes, word_tags_list = bot_corpus(words, classes, pattern_word_tags_list, ignore_symbols)
print("stem_words: ",stem_words)
print("tag_classes :",tag_classes)
print("word_tags_list:",word_tags_list)


def bag_of_words_encoding(stem_words, pattern_word_tags_list):
    
    bag = []
    for word_tags in pattern_word_tags_list:
        # example: word_tags = (['hi', 'there'], 'greetings']

        pattern_words = word_tags[0] # ['hi', 'there']
        stem_pattern_words = get_stem_words(pattern_words, ignore_symbols)
        bag_of_words = []

        for word in stem_words:            
            if word in stem_pattern_words:              
                bag_of_words.append(1)
            else:
                bag_of_words.append(0)
    
        bag.append(bag_of_words)
    
    return np.array(bag)
# train_x = bag_of_words_encoding(stem_words, word_tags_list)
# print(train_x[0])

def class_label_encoding(classes, pattern_word_tags_list):
    
    labels = []

    for word_tags in pattern_word_tags_list:

        # Start with list of 0s
        labels_encoding = list([0]*len(classes))  

        # example: word_tags = (['hi', 'there'], 'greetings']

        tag = word_tags[1]   # 'greetings'

        tag_index = classes.index(tag)

        # Labels Encoding
        labels_encoding[tag_index] = 1

        labels.append(labels_encoding)
        
    return np.array(labels)

# train_y = class_label_encoding(tag_classes, word_tags_list)
# print(train_y[5])


def preprocess_train_data():
  
    stem_words, tag_classes, word_tags_list = bot_corpus(words, classes, pattern_word_tags_list, ignore_symbols)
    
    # Convert Stem words and Classes to Python pickel file format
    pickle.dump(stem_words, open('words.pkl','wb'))
    pickle.dump(tag_classes, open('classes.pkl','wb'))

    train_x = bag_of_words_encoding(stem_words, word_tags_list)
    train_y = class_label_encoding(tag_classes, word_tags_list)
    
    return train_x, train_y

#preprocess_train_data()


