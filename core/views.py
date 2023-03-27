from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

from .models import News
from .forms import NewsForm

pac = joblib.load('modeling.sav')


def home_view(request):
    return render(request, 'core/home.html')

@login_required
def dashboard_view(request):
    if request.method == 'GET':
        form = NewsForm()
    checked_news = News.objects.all().order_by("-id")
    context={"form": form, "checked_news": checked_news}
    return render(request, 'core/dashboard.html', context)

@login_required
def result_view(request):
    form_param = request.GET
    news_content = form_param['content']

    ans = pac.predict(news_content)