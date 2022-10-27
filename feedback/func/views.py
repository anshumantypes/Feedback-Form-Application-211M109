from django.shortcuts import render
from .models import contactform
from django.core.mail import send_mail

# Create your views here.
def mailer(request):
    if request.method=='POST':
        ffname=request.POST.get('first')
        llname=request.POST.get('last')
        mail=request.POST.get('mail')
        pphone=request.POST.get('number')
        qquery=request.POST.get('query')
        en=contactform(fname=ffname,lname=llname,email=mail,phone=pphone,query=qquery)
        en.save()
        send_mail(
            f"thanks for contacting us",
            f'thanks for contacting us,\n{ffname} {llname}\n we recived the following feedback \n{qquery} \nwe will respond you soon',
            'anshumanu35@gmail.com',
            [mail],
            fail_silently=False,
        )

        return render(request,'feedback.html',{'message':'thanks for your response'})
    else:
        return render(request,'feedback.html',{})
