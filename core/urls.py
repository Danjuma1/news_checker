from django.urls import path
from . import views

app_name = "core"   

urlpatterns = [
    path("", views.home_view, name="home"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("result/", views.result_view, name="result"),
    # path("save/", views.save_view, name="save")
]
