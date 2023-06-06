# Importing an required libraries
from nltk.stem import WordNetLemmatizer
import os
import tqdm
import torch.utils.data as data_utils
import pandas as pd
import re
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer, util
import torch
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")

# Contraction Mapping Dictionary
contraction_mapping = {"that'll": "that will", "ain’t": "is not", "aren’t": "are not", "can’t": "cannot", "’cause": "because", "could’ve": "could have", "couldn’t": "could not",
                       "didn’t": "did not", "doesn’t": "does not", "don’t": "do not", "hadn’t": "had not", "hasn’t": "has not", "haven’t": "have not",
                       "he’d": "he would", "he’ll": "he will", "he’s": "he is", "how’d": "how did", "how’d’y": "how do you", "how’ll": "how will", "how’s": "how is",
                       "I’d": "I would", "I’d’ve": "I would have", "I’ll": "I will", "I’ll’ve": "I will have", "I’m": "I am", "I’ve": "I have", "i’d": "i would",
                       "i’d’ve": "i would have", "i’ll": "i will",  "i’ll’ve": "i will have", "i’m": "i am", "i’ve": "i have", "isn’t": "is not", "it’d": "it would",
                       "it’d’ve": "it would have", "it’ll": "it will", "it’ll’ve": "it will have", "it’s": "it is", "let’s": "let us", "ma’am": "madam",
                       "mayn’t": "may not", "might’ve": "might have", "mightn’t": "might not", "mightn’t’ve": "might not have", "must’ve": "must have",
                       "mustn’t": "must not", "mustn’t’ve": "must not have", "needn’t": "need not", "needn’t’ve": "need not have", "o’clock": "of the clock",
                       "oughtn’t": "ought not", "oughtn’t’ve": "ought not have", "shan’t": "shall not", "sha’n’t": "shall not", "shan’t’ve": "shall not have",
                       "she’d": "she would", "she’d’ve": "she would have", "she’ll": "she will", "she’ll’ve": "she will have", "she’s": "she is",
                       "should’ve": "should have", "shouldn’t": "should not", "shouldn’t’ve": "should not have", "so’ve": "so have", "so’s": "so as",
                       "this’s": "this is", "that’d": "that would", "that’d’ve": "that would have", "that’s": "that is", "there’d": "there would",
                       "there’d’ve": "there would have", "there’s": "there is", "here’s": "here is", "they’d": "they would", "they’d’ve": "they would have",
                       "they’ll": "they will", "they’ll’ve": "they will have", "they’re": "they are", "they’ve": "they have", "to’ve": "to have",
                       "wasn’t": "was not", "we’d": "we would", "we’d’ve": "we would have", "we’ll": "we will", "we’ll’ve": "we will have", "we’re": "we are",
                       "we’ve": "we have", "weren’t": "were not", "what’ll": "what will", "what’ll’ve": "what will have", "what’re": "what are",
                       "what’s": "what is", "what’ve": "what have", "when’s": "when is", "when’ve": "when have", "where’d": "where did", "where’s": "where is",
                       "where’ve": "where have", "who’ll": "who will", "who’ll’ve": "who will have", "who’s": "who is", "who’ve": "who have",
                       "why’s": "why is", "why’ve": "why have", "will’ve": "will have", "won’t": "will not", "won’t’ve": "will not have",
                       "would’ve": "would have", "wouldn’t": "would not", "wouldn’t’ve": "would not have", "y’all": "you all",
                       "y’all’d": "you all would", "y’all’d’ve": "you all would have", "y’all’re": "you all are", "y’all’ve": "you all have",
                       "you’d": "you would", "you’d’ve": "you would have", "you’ll": "you will", "you’ll’ve": "you will have",
                       "you’re": "you are", "you’ve": "you have", "ain't": "is not", "aren't": "are not", "can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not",
                       "didn't": "did not", "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not",
                       "he'd": "he would", "he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",
                       "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have", "I'm": "I am", "I've": "I have", "i'd": "i would",
                       "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have", "i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would",
                       "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have", "it's": "it is", "let's": "let us", "ma'am": "madam",
                       "mayn't": "may not", "might've": "might have", "mightn't": "might not", "mightn't've": "might not have", "must've": "must have",
                       "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have", "o'clock": "of the clock",
                       "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have",
                       "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is",
                       "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have", "so's": "so as",
                       "this's": "this is", "that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would",
                       "there'd've": "there would have", "there's": "there is", "here's": "here is", "they'd": "they would", "they'd've": "they would have",
                       "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have",
                       "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are",
                       "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",
                       "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is",
                       "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have",
                       "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have",
                       "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all",
                       "y'all'd": "you all would", "y'all'd've": "you all would have", "y'all're": "you all are", "y'all've": "you all have",
                       "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have",
                       "you're": "you are", "you've": "you have", "n't": 'not'}


class preprocessing:
    def lemmatization(sentence):
        """ 
            lemmatization() function takes a string as input 
            and returns the string after doing lemmatization
            Input : "who makes these"
            Output : "who make these"
        """
        wordnet_lemmatizer = WordNetLemmatizer()
        word_list = []

        # Iterating through each word in the sentence
        for word in sentence.split():
            word = wordnet_lemmatizer.lemmatize(word, 'v')
            word = wordnet_lemmatizer.lemmatize(word, 'n')
            word_list.append(word)
        return " ".join(word_list)

    def remove_punctuation(self, text_data):
        # removing an punctuation from text
        pattern = re.compile(r"[^A-Za-z0-9 ]")
        train_data = pattern.sub("", text_data)
        return train_data

    def normalize_text_data(self, text_data):
        x = text_data.lower()  # lower-casing the words
        word_list = []

        # Iterating through each word in the sentence
        for word in x.split():      # contraction mapping
            if word in contraction_mapping:
                word_list.append(contraction_mapping[word])
            else:
                word_list.append(word)

        x = ' '.join(word_list)
        # removing 's, Example : it's --> it
        x = re.sub("'s", ' ', x)
        # removing newline character
        x = re.sub('\n', ' ', x)
        # removing non-alphabetic characters
        x = re.sub(r'[^a-z]', ' ', x)
        # replacing multiple spaces with single spaces
        x = re.sub(r'\s+', ' ', x)
        # Removing leftmost and rightmost spaces
        text_data = x.strip()
        return ''.join(text_data.lower().strip())

    def stopwords_add_remove(self, lang="english", new_stopwords=''):
        # Initializing stopwords
        stop_words = set()
        if new_stopwords:
            # adddig multiple stopwords
            stop_words = stop_words.union(new_stopwords)
        return stop_words

    def removing_text_stopwords(self, text_data, stop_words):
        # Removing stopwords from text_data
        return ' '.join([text for text in text_data.split() if text not in stop_words])

    def replace_words(self, text_data, old_word, new_word):
        # Replacing old word with new word
        return ' '.join([text.replace(old_word, new_word, -1) for text in text_data.split()])


class Model_Buiding_approach:
    def __init__(self, industry=None, country=None, model_name='bert-base-uncased'):
        self.industry = industry
        self.country = country
        self.model_name = model_name

    def preprocess_example(self, question):

        # Passing an stopwords
        new_stopwords = ['a', 'an', 'the', 'please', 'pitney', 'bowes']

        prep = preprocessing()
#         text = prep.remove_punctuation(question)

        # Converting an short forms into long forms
        dict_words = {'HCM': 'Human Capital Management',
                      'ERP': 'Enterprise Resource Planning', 'SCM': 'Supply Chain Management'}
        for key, value in dict_words.items():
            text = prep.replace_words(question, old_word=key, new_word=value)

        # Lower the text and apply sample cleanings
        text = prep.normalize_text_data(text)
        print("Cleaned Text", text)
        print("-------------------------------")

        # creating an stopwords
        stop_words = prep.stopwords_add_remove(new_stopwords=new_stopwords)

        # Remove stopwords
        text = prep.removing_text_stopwords(text, stop_words)

        return text

    def dataset_preprocessing_and_embedding(self, df, embedder):
        # Calling the preprocessing
        df['Preprocessed_question'] = df["question"].apply(
            self.preprocess_example)

        corpus_embeddings = embedder.encode(
            list(df['Preprocessed_question']), convert_to_tensor=True)

        # Checking the Directories structures
        if os.path.isdir('RFP/Embedding Models/'):
            print(
                "-------------------RFP/Embedding Models/ is present------------------------")
        else:
            print("--------------------------Directory is not present-----------")
            os.mkdir('RFP/Embedding Models/')

        if os.path.isdir('RFP/Preprocessed_Files/'):
            print(
                "-------------------RFP/Preprocessed_Files/ is present------------------------")
        else:
            print("--------------------------Directory is not present-----------")
            os.mkdir('RFP/Preprocessed_Files/')

        torch.save(corpus_embeddings, "RFP/Embedding Models/corpus_embedding" +
                   '-'+self.model_name+'-'+self.country+"-"+self.industry+".pt")
        df.to_excel('./RFP/Preprocessed_Files/Preprocessed-'+self.model_name +
                    '-'+self.country+'-'+self.industry+".xlsx", index=False)
        print("Dataset Preprocessinng and Embedding is Done")
        return df

    def embedding_data(self, text, embedder):
        text = embedder.encode(text, convert_to_tensor=True)
        return text

    def new_query_preprocess_similarity(self, df, query, embedder,  top=3, threshold=0.5):

        print(df.shape)

        # calling preprocessing on query
        query_preprocessed = self.preprocess_example(query)

        index_list = []
        cos_sim_list = []
        # Reading an corpus
        if os.path.isdir('RFP/Embedding Models/'):
            print(
                "-------------------RFP/Embedding Models/ is present------------------------")
            corpus_embeddings = torch.load(
                'RFP/Embedding Models/corpus_embedding'+'-'+self.model_name+'-'+self.country+'-'+self.industry+'.pt')

            # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
            top_k = min(top, len(corpus_embeddings))

            query_embedding = embedder.encode(
                query_preprocessed, convert_to_tensor=True)

            # We use cosine-similarity and torch.topk to find the highest 5 scores
            cos_scores = util.pytorch_cos_sim(
                query_embedding, corpus_embeddings)[0]
            top_results = torch.topk(cos_scores, k=top_k)

            print("\n\n======================\n\n")
            print("Query:", query)
            print("\nTop 3 most similar sentences in corpus:")

            for score, idx in zip(top_results[0], top_results[1]):
                if score >= threshold:
                    print("-------------------")
#                     print("questions:- ",df['question'][int(idx)],"(Score: {:.4f}%)".format(score*100))
                    print("Document Link:- ", df['document_link']
                          [int(idx)], "(Score: {:.4f}%)".format(score*100))
                    index_list.append(int(idx))
                    cos_sim_list.append("{:.4f}%".format(score*100))
            if len(index_list) == 0:
                return index_list, cos_sim_list
            if len(index_list) < top:
                for index in range(top-len(index_list)):
                    print("-------------------")
                    print("No question Found")
                    #index_list.append("No Index Found")

                    # cos_sim_list.append("0")
        else:
            print("--------------------------Directory is not present-----------")

        return index_list, cos_sim_list

    def training_dataset_vector(self, df, embedder):
        start = time.time()

        # dataset_preprocessing and embedding
        df = self.dataset_preprocessing_and_embedding(df=df, embedder=embedder)
        end = time.time()
        print("Time taken for Embedding:- ", end-start)
        return end-start

    def dataframe_filter_return(self, df, industry=None, country=None, section_data=None):
        # Filtering Data based on industry, country and section_data
        if (df['industry'].isin(industry).any()) and (df['country'].isin(country).any()) and (df['section_data'].isin(section_data).any()):
            print("All three filter applied (industry, country, section_data)")
            print("Filter Applied = {country:", str(
                country), ", industry:"+str(industry)+", section_data:"+str(section_data)+"}")
            df = df[(df['industry'].isin(industry)) & (df['country'].isin(
                country)) & (df['section_data'].isin(section_data))]

        elif (df['industry'].isin(industry).any()) and (df['country'].isin(country).any()):
            print("All three filter applied (industry, country)")
            print("Filter Applied = {country:", str(
                country), ", industry:"+str(industry)+"}")
            df = df[(df['industry'].isin(industry))
                    & (df['country'].isin(country))]

        elif (df['country'].isin(country).any()) and (df['section_data'].isin(section_data).any()):
            print("AND Filter Applied = {country:", str(
                country), ", industry:"+str(industry)+"}")
            df = df[(df['country'].isin(country)) & (
                df['section_data'].isin(section_data))]

        elif (df['industry'].isin(industry).any()) and (df['section_data'].isin(section_data).any()):
            print("AND Filter Applied = {country:", str(
                country), ", industry:"+str(industry)+"}")
            df = df[(df['industry'].isin(country)) & (
                df['section_data'].isin(section_data))]

        elif (df['industry'].isin(industry).any()) or (df['country'].isin(country).any()) or (df['section_data'].isin(section_data).any()):
            print("Any one of three filter applied (industry, country, section_data)")
            print("Filter Applied = {country:", str(
                country), ", industry:"+str(industry)+", section_data:"+str(section_data)+"}")
            df = df[(df['industry'].isin(industry)) | (df['country'].isin(
                country)) | (df['section_data'].isin(section_data))]
        else:
            print("No Filtered Applied")

        df = df.reset_index(drop='index')
        return df

    def query_resolved(self, query, df, embedder):
        start = time.time()
        index_list, cos_sim_list = self.new_query_preprocess_similarity(
            df, query, top=3, embedder=embedder)
        end = time.time()
        print("Time taken for query resolve is", end-start)
        return index_list, cos_sim_list
