from django.shortcuts import render


def home_view(request):
    return render(request, 'core/home.html')

def dashboard_view(request):
    return render(request, 'core/dashboard.html')
