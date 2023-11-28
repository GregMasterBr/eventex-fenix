from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk, Course
from django.views.generic import View, TemplateView
from django.views.generic.base import TemplateResponseMixin

class GenericHomeView(TemplateView):
    object_list = None
    context_object_name = None
  
    def get_context_data(self, **kwargs):
        context =  { self.context_object_name: self.object_list}
        context.update(kwargs)
        return context

class HomeView(GenericHomeView):
    template_name = 'index.html'
    object_list = Speaker.objects.all() 
    context_object_name = 'speaker_list'    


def speaker_detail(request, slug):
    #speaker = Speaker.objects.get(slug=slug)
    speaker = get_object_or_404(Speaker, slug=slug)
 
    return render(request,"core/speaker_detail.html", {'speaker': speaker})


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    } 
    return render(request,"core/talk_list.html", context)


def contato(request):
    return render(request,"contato.html")    