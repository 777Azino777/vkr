from django.shortcuts import render,get_object_or_404, loader,HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.models import User
from persons.forms import An_form
from persons.models import anonim_message
# Create your views here.

def an_message(request):
    args={}
    args['form'] = An_form
    args['text'] = anonim_message.objects.all()
    args['username'] =auth.get_user(request).username
    args['an_page'] = 'active'
    if request.method == 'POST':
        form =  An_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/an_ms/')
    return render(request,'anonim_ms.html',args)


