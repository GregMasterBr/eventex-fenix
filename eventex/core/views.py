from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk, Course
from django.views.generic import ListView


home = ListView.as_view(template_name='index.html', model=Speaker)

def speaker_detail(request, slug):
    #speaker = Speaker.objects.get(slug=slug)
    speaker = get_object_or_404(Speaker, slug=slug)
 
    return render(request,"core/speaker_detail.html", {'speaker': speaker})


talk_list = ListView.as_view(model=Talk)

def contato(request):
    return render(request,"contato.html")    