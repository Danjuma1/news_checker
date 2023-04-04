from django.urls import path
from . import views

app_name = "core"   

urlpatterns = [
    path("", views.home_view, name="home"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    # path("result/", views.result_view, name="result"),
    path("all_news/", views.news_list_view, name="news_list"),
    path("all_true_news/", views.true_news_list_view, name="true_news_list"),
    path("all_fake_news/", views.fake_news_list_view, name="fake_news_list"),
]
