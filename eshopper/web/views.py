from django.shortcuts import render
from .models import Client,Carosuel
from .forms import ContactForm
from django.http import JsonResponse
import urllib.parse
# Create your views here.


def index(request):
    client = Client.objects.all()
    Carousel = Carosuel.objects.all()
    context = {
        'clients':client,
        'Carosuel':Carousel
    }
    return render(request,'web/index.html',context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
                        
            # watsapp message

            # watsapp_message={
            #     f"Name : {form.name}\n"
            #     f"email:{form.email}\n"
            #     f"subject:{form.subject}\n"
            #     f"message:{form.msg}\n"
            # }
            # watsapp_api_url='https://api.watsapp.com/send'
            # phone_number

            response_data={
              'status':'true',
              'title' :'succesfully submite',
              'message':"message succesfully submite"
          }
        else:
            response_data={
               'status':'false',
               'title': "oops !",
               'message':"oops !"
        }


        return JsonResponse(response_data)
    
    context={
        'form':form
    }
    return render(request,'web/contact.html',context)

def shop(request):
    return render(request,'web/shop.html')


