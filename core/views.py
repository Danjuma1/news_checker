from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User


import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import pandas as pd
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('wordnet')

import re
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import pickle

from .models import News
from .forms import NewsForm

from accounts.models import UserProfile

stop_words = set(stopwords.words('english'))

# tfidf_vectorizer = TfidfVectorizer
# pac = joblib.load('modeling.sav')

clf2 = pickle.load(open("model.pkl", "rb"))
vectorizer=pickle.load(open("vectorizer.pickle", 'rb'))

def LemmSentence(sentence):
    lemma_words = []
    wordnet_lemmatizer = WordNetLemmatizer()
    word_tokens = word_tokenize(sentence)
    for word in word_tokens:
        if word not in stop_words:
            new_word = re.sub('[^a-zA-Z]', '', word)
            new_word = new_word.lower()
            new_word = wordnet_lemmatizer.lemmatize(new_word)
            lemma_words.append(new_word)
    return " ".join(lemma_words)


def output_lable(n):
    if n == 1:
        return "Fake News"
    elif n == 0:
        return "True News"


def manual_testing(news):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(LemmSentence)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorizer.transform(new_x_test)
    pred_DT = clf2.predict(new_xv_test)
    return output_lable(pred_DT)

def home_view(request):
    return render(request, 'core/home.html')

@login_required
def dashboard_view(request):
    out =''
    form = NewsForm()
    user = request.user
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            # sent_news = form.save()
            redirect('/')
            headline = form.cleaned_data.get('headline')
            author = form.cleaned_data.get('author')
            content = form.cleaned_data.get('content')
            out = manual_testing(content)
            label = out
            saved_news = News.objects.create(user=user, headline=headline, author=author, content=content, label=label)
            saved_news.save()

    checked_news = News.objects.all().order_by("-id")
    context={"form": form,
            'output': out, 
            "checked_news": checked_news,
    }
    return render(request, 'core/dashboard.html', context)


# def result_view(request):
#     out = request.session['out']
#     context = {
#         'output': out
#     }
#     return render(request, 'core/result.html', context)

def home(request):
    news = News.objects.all()

    context = {
        'news': news,
    }
    
    return render(request, 'core/home.html', context)


@login_required
def news_list_view(request):
    all_news = News.objects.all().order_by("-id")

    context = {
        'all_news': all_news,
    }
    
    return render(request, 'core/all_news_list.html', context)

@login_required
def true_news_list_view(request):
    true_news = News.objects.all().filter(label="True News")

    context = {
        'true_news': true_news,
    }
    
    return render(request, 'core/true_news_list.html', context)

@login_required
def fake_news_list_view(request):
    fake_news = News.objects.all().filter(label="Fake News")

    context = {
        'fake_news': fake_news,
    }
    
    return render(request, 'core/fake_news_list.html', context)


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = UserProfile.objects.filter(user=user)
    posts = News.objects.filter(user=user).order_by('-date_added')

    context = {
        'user': user,
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'core/profile.html', context)

@login_required
def news_delete_view(request, news_id):
    news = get_object_or_404(News, id=news_id)
    user = request.user.username 

    if request.method == 'POST':
        news.delete()
        return redirect('core:profile',user)
    
    context = {
        'news': news,
    }
    return render(request, 'core/news_delete.html', context)


@login_required
def each_news_view(request, news_id):
    news = get_object_or_404(News, id=news_id)
    context = {
        'news': news,
    }
    return render(request, 'core/each_news.html', context)

def outside_news_views(request):
    all_news = News.objects.all().order_by("-id")

    context = {
        'all_news': all_news,
    }
    
    return render(request, 'core/outside_news.html', context)