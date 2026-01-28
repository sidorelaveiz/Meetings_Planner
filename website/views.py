from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meetings


# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meetings": Meetings.objects.count()})



# def welcome(request):
#     meetings = Meetings.objects.all()
#     context:{
#         'meetings' : meetings
#     }
#     return render(request, "website/welcome.html", context)



def date(request):
    return HttpResponse("Server date " + str(datetime.now()))
