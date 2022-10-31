import pandas as pd
import nltk
import numpy as np
import re
from nltk.stem import wordnet # to perform lemmitization
from sklearn.feature_extraction.text import CountVectorizer # to perform bow
from sklearn.feature_extraction.text import TfidfVectorizer # to perform tfidf
from nltk import pos_tag # for parts of speech
from sklearn.metrics import pairwise_distances # to perfrom cosine similarity
from nltk import word_tokenize # to create tokens
from nltk.corpus import stopwords # for stop words


def text_normalization(text):
    text = str(text).lower()  # text to lower case
    spl_char_text = re.sub(r'[^ a-z]', '', text)  # removing special characters
    tokens = word_tokenize(spl_char_text)  # word tokenizing
    lema = wordnet.WordNetLemmatizer()  # intializing lemmatization
    tags_list = pos_tag(tokens, tagset=None)  # parts of speech
    lema_words = []  # empty list
    for token, pos_token in tags_list:
        if pos_token.startswith('V'):  # Verb
            pos_val = 'v'
        elif pos_token.startswith('J'):  # Adjective
            pos_val = 'a'
        elif pos_token.startswith('R'):  # Adverb
            pos_val = 'r'
        else:
            pos_val = 'n'  # Noun
        lema_token = lema.lemmatize(token, pos_val)  # performing lemmatization
        lema_words.append(lema_token)  # appending the lemmatized token into a list

    return " ".join(lema_words)  # returns the lemmatized tokens as a sentence

def stopword_(text):
    tag_list=pos_tag(nltk.word_tokenize(text),tagset=None)
    stop=stopwords.words('english')
    lema=wordnet.WordNetLemmatizer()
    lema_word=[]
    for token,pos_token in tag_list:
        if token in stop:
            continue
        if pos_token.startswith('V'):
            pos_val='v'
        elif pos_token.startswith('J'):
            pos_val='a'
        elif pos_token.startswith('R'):
            pos_val='r'
        else:
            pos_val='n'
        lema_token=lema.lemmatize(token,pos_val)
        lema_word.append(lema_token)
    return " ".join(lema_word)

def chat_bow(text):
    cv = CountVectorizer()
    X = cv.fit_transform(df['lemmatized_text']).toarray()
    features = cv.get_feature_names()
    df_bow = pd.DataFrame(X, columns = features)
    s=text
    #s=stopword_(text)
    lemma=text_normalization(s) # calling the function to perform text normalization
    bow=cv.transform([lemma]).toarray() # applying bow
    cos = 1- pairwise_distances(df_bow,bow, metric = 'cosine' )
    index_value=cos.argmax() # getting index value
    value=cos.max()
    return value,df['Text Response'].loc[index_value]

def chat_tfidf(text):
    tfidf = TfidfVectorizer()  # intializing tf-id
    x_tfidf = tfidf.fit_transform(df['lemmatized_text']).toarray()  # transforming the data into array
    df_tfidf = pd.DataFrame(x_tfidf, columns=tfidf.get_feature_names())
    s=text
    #s = stopword_(text)
    lemma=text_normalization(s) # calling the function to perform text normalization
    tf=tfidf.transform([lemma]).toarray() # applying tf-idf
    cos=1-pairwise_distances(df_tfidf,tf,metric='cosine') # applying cosine similarity
    index_value=cos.argmax() # getting index value
    value=cos.max()
    return value,df['Text Response'].loc[index_value]

def get_respoonse(question):
    bow_v,bow_ans=chat_bow(question)
    tfidf_v,tfidf_ans=chat_tfidf(question)
    if bow_v>tfidf_v and bow_v>0.2:
        return bow_ans
    elif bow_v<=tfidf_v and tfidf_v>0.2:
        return tfidf_ans
    else:
        return "Sorry, I don't know the answer. Could you please change the question?"

df=pd.read_excel('diagnosis\Colon adenocarcinoma-1.xlsx')
df.ffill(axis = 0,inplace=True)
df['lemmatized_text']=df['Context'].apply(text_normalization)
Question = 'what cancer do I have'
print(get_respoonse(Question))