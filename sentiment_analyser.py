import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','p4.settings')
import django
django.setup()

from nltk.corpus import stopwords
import nltk
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def Word_Tokenization(text):
    return word_tokenize(text)

#Removing Stopwords
stop_words=set(stopwords.words("english"))
def Removing_Stopwords(List):
    filtered_sent=''
    for w in List:
        if w not in stop_words:
            filtered_sent+=w+' '
    return filtered_sent

analyser = SentimentIntensityAnalyzer()
def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    List = list()
    List.append(['',''])
    List.append(['Positive',float(100*score['pos'])])
    List.append(['Negative',float(score['neg']*100)])
    List.append(['Neutral',float(score['neu']*100)])
    return List

def pos_tagging(List):
    return nltk.pos_tag(List)

def freq_dist(List):
    fd = nltk.FreqDist(List)
    l=list()
    l.append(['',''])
    for i in fd:
        l.append([i,fd[i]])
    return l
