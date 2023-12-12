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
from django.views.generic import CreateView
from django.shortcuts import resolve_url as r


class SubscriptionCreate(CreateView):
   model = Subscription
   form_class = SubscriptionForm

   def form_valid(self, form):
      response = super().form_valid(form)
      self.send_mail()

      return response
   
   def send_mail(self):
      '''Send subscription email '''
      subject = 'Confirmação de inscrição'
      from_ = settings.DEFAULT_FROM_EMAIL
      to = self.object.email
      template_name = 'subscriptions/subscription_email.txt'
      context = {'subscription':self.object}

      body = render_to_string(template_name, context)
      return mail.send_mail(subject, body, from_, [from_, to])
       
     
new = SubscriptionCreate.as_view()

detail = DetailView.as_view(model=Subscription)

