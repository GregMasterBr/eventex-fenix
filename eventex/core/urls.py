from django.urls import path
from eventex.core import views
urlpatterns = [
    path("", views.home, name="home"),
    path("contato", views.contato, name="contato"),
]