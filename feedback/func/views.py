from django.shortcuts import render
from .models import contactform

# Create your views here.
def mailer(request):
    if request.method=='POST':
        fname=request.POST['first']
        lname=request.POST['last']
        email=request.POST['mail']
        phone=request.POST['number']
        query=request.POST['query']

        return render(request,'feedback.html',{'message':fname})
    else:
        return render(request,'feedback.html',{})
