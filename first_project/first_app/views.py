from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,User
# Create your views here.

def index(request):
    return HttpResponse("<em> My Second App </em>");

def help(request):
    web = AccessRecord.objects.order_by('date')
    dict = {'var1':web}
    return render(request,'first_app/index.html',context=dict)

def user(request):
    userlist = User.objects.order_by('first_name')
    dict = {'user':userlist}
    return render(request,'first_app/user.html',context=dict)
