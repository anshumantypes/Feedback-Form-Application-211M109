from django.shortcuts import render

# Create your views here.
def mailer(request):
    return render(request,'feedback.html')