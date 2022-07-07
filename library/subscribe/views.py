from django.shortcuts import render

from django.shortcuts import render
from library.settings import EMAIL_HOST_USER

from .import forms
from django.core.mail import send_mail

# Create your views here.
def subscribe(request):
    sub=forms.Subscribe()#A sub is a form object. We are checking whether the data received is GET or POST. If the method is GET, it will give an empty form, otherwise, it will execute the code in if statement.
    
    if request.method=="POST":
        sub=forms.Subscribe(request.POST)
        subject="Welcome To Data web developement"
        message="Hope will enjoy the your Django course"
        
        recepient=str(sub['Email'].value())
        
        send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
        return render(request,'subscribe/success.html',{'recipient':recepient})
    return render(request,'subscribe/index.html',{'form':sub})
    
    