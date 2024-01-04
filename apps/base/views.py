from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.contrib.auth import logout
# Create your views here.
from django.http import HttpResponseRedirect

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/admin/')

def admin_view(request):
    return HttpResponseRedirect('/admin/')