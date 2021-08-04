from django.shortcuts import render, HttpResponse

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
    # return HttpResponse("This is contact page")
    return render(request,'contact.html')
