import json
import urllib
from urllib import parse
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.http import Http404
from MapApp.models import myServerMap
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	return HttpResponse("hello,ServerMap!")