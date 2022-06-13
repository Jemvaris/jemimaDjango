from django.urls import path
from jemvarisapp import views
urlpatterns = [
    path("", views.home, name="home"),
]