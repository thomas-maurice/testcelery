from django.shortcuts import render
from django.http import HttpResponse
import utils.tasks

# Create your views here.
def home(request):
    try:
        utils.tasks.send_email.delay("data :)")
        return HttpResponse('woot !')
    except:
        return HttpResponse('fail !')
