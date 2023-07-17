from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages

def subscribe(request):
   context = {'form':SubscriptionForm()}
   return render(request,'subscriptions/subscription_form.html',context)    