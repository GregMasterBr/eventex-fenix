from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker

def home(request):
    speakers = Speaker.objects.all()    
    return render(request,"index.html", {'speaker_list': speakers})


def speaker_detail(request, slug):
    #speaker = Speaker.objects.get(slug=slug)
    speaker = get_object_or_404(Speaker, slug=slug)
 
    return render(request,"core/speaker_detail.html", {'speaker': speaker})


def contato(request):
    return render(request,"contato.html")    