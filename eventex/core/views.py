from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk, Course

def home(request):
    speakers = Speaker.objects.all()    
    return render(request,"index.html", {'speaker_list': speakers})


def speaker_detail(request, slug):
    #speaker = Speaker.objects.get(slug=slug)
    speaker = get_object_or_404(Speaker, slug=slug)
 
    return render(request,"core/speaker_detail.html", {'speaker': speaker})


def talk_list(request):
    at_morning = list(Talk.objects.at_morning())
    at_morning.sort(key=lambda o:o.start)
    at_afternoon = list(Talk.objects.at_afternoon())
    at_afternoon.sort(key=lambda o:o.start)
    context = {
        'morning_talks': at_morning,
        'afternoon_talks': at_afternoon,
    } 
    return render(request,"core/talk_list.html", context)


def contato(request):
    return render(request,"contato.html")    