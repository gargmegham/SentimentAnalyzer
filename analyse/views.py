from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
import sentiment_analyser
import json

def index(request):
    user_input = userinput()
    return render(request, "analyse/index.html", {'input_sentence': user_input})

def analyse(request):
    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        input_sentence = user_input.cleaned_data['q']
        word_List = sentiment_analyser.Word_Tokenization(input_sentence)
        no_stop_words = sentiment_analyser.Removing_Stopwords(word_List)
        score = sentiment_analyser.sentiment_analyzer_scores(no_stop_words)
        data_dump = json.dumps(dict({'':input_sentence}))
        with open('phrase.json', 'w') as json_file:
            json.dump(data_dump, json_file)
        pos_tagged = sentiment_analyser.pos_tagging(word_List)
        freqWords = sentiment_analyser.freq_dist(word_List)
        context= {
                    'score': score,
                    'word_List':word_List,
                     'no_stop_words':no_stop_words,
                     'pos_tagged':pos_tagged,
                     'freqWords':freqWords,
        }
        return render(request, "analyse/analyse.html", context)
    return render(request, "analyse/index.html", {'input_sentence': user_input})
