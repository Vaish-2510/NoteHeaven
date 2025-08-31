
from django.shortcuts import render,HttpResponse
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1' : "this is sent",
        "variable2" : "Hey Bro"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is Homepage")
def about(request):
     return render(request, 'about.html')
    # return HttpResponse("This is Aboutpage")
def services(request):
     return render(request, 'services.html')
    # return HttpResponse("This is Services page")
def contact(request):
     if request.method=="POST":
        
         email=request.POST.get('email')
         password=request.POST.get('password')
         contact = Contact(password=password,email=email)
         contact.save()
         messages.success(request, "Your message has been sent!")
      
     return render(request, 'contact.html')
    # return HttpResponse("This is Contact page")""