from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Host
from django.contrib.auth.models import User
from collections import Counter


def home(request):
    template_name = "home.html"
    username = request.user.get_username()
    host_obj = Host.objects.all().filter(username=username)
    context = {"host_obj": host_obj, "username": username}
    return render(request, template_name, context)
