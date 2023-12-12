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
from django.views.generic.edit import BaseCreateView
from django.shortcuts import resolve_url as r


class SubscriptionCreate(TemplateResponseMixin, BaseCreateView):
   template_name = 'subscriptions/subscription_form.html'
   form_class = SubscriptionForm

   def form_valid(self, form):
      response = super().form_valid(form)

      #envia email
      _send_mail('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, self.object.email, 'subscriptions/subscription_email.txt', {'subscription':self.object})
      
      return response
   
     
new = SubscriptionCreate.as_view()

detail = DetailView.as_view(model=Subscription)

def _send_mail(subject, from_, to, template_name, context):
      body = render_to_string(template_name, context)
      mail.send_mail(subject, body, from_, [from_, to])

