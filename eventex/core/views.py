from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk, Course
from django.views.generic import ListView, DetailView


home = ListView.as_view(template_name='index.html', model=Speaker)

speaker_detail = DetailView.as_view(model=Speaker)

talk_list = ListView.as_view(model=Talk)

def contato(request):
    return render(request,"contato.html")    