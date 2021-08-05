from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {  # sending user value to html page ***
        'var1':'Akash',
        'var2':'Suwar'
    }
    # return HttpResponse("This is home page")
    return render(request,'index.html',context)
    
def about(request):
    # return HttpResponse("This is about page")
    return render(request,'about.html')


def service(request):
    # return HttpResponse("This is service page")
    return render(request,'service.html')


def contact(request):
    # wriiting method forr taking input from form 

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()

        messages.success(request, 'Request Submited')

    # return HttpResponse("This is contact page")
    return render(request,'contact.html')
