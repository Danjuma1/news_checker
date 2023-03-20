from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import News
from .forms import NewsForm


def home_view(request):
    return render(request, 'core/home.html')

@login_required
def dashboard_view(request):
    checked_news = News.objects.all().order_by("-id")
    form = NewsForm
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("core:dashboard")
    context={"form": form, "checked_news": checked_news}
    return render(request, 'core/dashboard.html', context)
