from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker, Talk, Course
from django.views.generic import View 

class HomeView(View):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)
    
    def render_to_response(self, context):
        return render(self.request, self.template_name, context)
    
    def get_context_data(self, **kwargs):
        speakers = Speaker.objects.all()    
        context =  {'speaker_list': speakers}
        context.update(kwargs)
        return context
    


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