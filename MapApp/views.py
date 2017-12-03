import json
import time
import urllib
from urllib import parse
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import Http404
from MapApp.models import myServerMap
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
	return render(request, 'login.html')

@csrf_exempt
def verifyLogin(request):
	if request.method == "GET":
	    userNo = request.GET.get("userNo","")
	    passwd = request.GET.get("passwd","")
	if request.method == "POST":
		data = json.loads(request.body.decode("utf-8"))
		userNo = data['userNo']
		passwd = data['passwd']
	print('userNo',userNo)
	print('passwd',passwd)
	user = authenticate(request,username = userNo, password = passwd)
	if user is not None:
		auth_login(request,user)
		sessionId=request.session.session_key 
		response = {'result':True, 'sessionId':sessionId}
		return HttpResponse(json.dumps(response), content_type='application/json;charset=utf-8')
	else:
		response = {'result':False, 'error': "username or password is error!"}
		return HttpResponse(json.dumps(response), content_type='application/json;charset=utf-8')

@csrf_exempt
def userLoginOut(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	logout(request)
	return HttpResponse(json.dumps({'ret':True}), content_type='application/json;charset=utf-8')

def index(request):
	if not request.user.is_authenticated:
		return redirect('/login')
	hostList = myServerMap.objects.all()
	return render(request, 'index.html', {'hostList' : hostList})

