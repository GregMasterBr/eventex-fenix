from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, resolve_url as r
from django.views.generic import DetailView, View

class SubscriptionCreate(View):
   def get(self, *args, **kwargs):
      return render(self.request,'subscriptions/subscription_form.html', {'form':SubscriptionForm()}) 

   def post(self, *args, **kwargs):
      form = SubscriptionForm(self.request.POST)

      if not form.is_valid():
         return render(self.request,'subscriptions/subscription_form.html', {'form':form})

      subscription = form.save() # quando o formulário for muito alinhado com a model.

      #envia email
      _send_mail('Confirmação de inscrição', settings.DEFAULT_FROM_EMAIL, subscription.email, 'subscriptions/subscription_email.txt', {'subscription':subscription})
      
      return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))
   
new = SubscriptionCreate.as_view()

detail = DetailView.as_view(model=Subscription)

def _send_mail(subject, from_, to, template_name, context):
      body = render_to_string(template_name, context)
      mail.send_mail(subject, body, from_, [from_, to])

