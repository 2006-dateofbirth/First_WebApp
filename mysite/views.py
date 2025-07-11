import operator
from django.shortcuts import render
from . import counter

def home(request):
    return render(request, 'index.html', {'key1': 'I am coming from python code'})

def result(request):
    article = request.GET['article']
    sorted_words, word_count = counter.count(article)

    return render(request, 'result.html', {
        'article': article,
        'word_count': word_count,
        'dict_words': sorted_words
    })
