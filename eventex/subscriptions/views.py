from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.views.generic import DetailView, View
from django.views.generic.base import TemplateResponseMixin
from django.shortcuts import resolve_url as r


class SubscriptionCreate(TemplateResponseMixin,View):
   template_name = 'subscriptions/subscription_form.html'
   form_class = SubscriptionForm

   
   def get(self, *args, **kwargs):
      return self.render_to_response(self.get_context_data()) 


   def post(self, *args, **kwargs):
      form = self.get_form()

      if not form.is_valid():
         return self.form_invalid(form)
      return self.form_valid(form)   
      

   def form_invalid(self, form):   
      return self.render_to_response(self.get_context_data(form=form))

   def form_valid(self, form):
      self.subscription = form.save() # quando o formulário for muito alinhado com a model.

      #envia email
      _send_mail('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, self.subscription.email, 'subscriptions/subscription_email.txt', {'subscription':self.subscription})
      
      return HttpResponseRedirect(self.get_success_url())
   

   def get_success_url(self):
       return self.subscription.get_absolute_url()
   
   
   def get_form(self):
       if self.request.method == 'POST':
           return self.form_class(self.request.POST)
       return self.form_class()
   
   def get_context_data(self, **kwargs):
       context = dict(kwargs)
       context.setdefault('form', self.get_form())
       return context
      
new = SubscriptionCreate.as_view()

detail = DetailView.as_view(model=Subscription)

def _send_mail(subject, from_, to, template_name, context):
      body = render_to_string(template_name, context)
      mail.send_mail(subject, body, from_, [from_, to])

