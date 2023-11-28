from django.urls import path
from eventex.core.views import contato, home
urlpatterns = [
    path("", home, name="home"),
    path("contato", contato, name="contato"),
]