from django.urls import path
from eventex.core.views import contato, HomeView
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contato", contato, name="contato"),
]