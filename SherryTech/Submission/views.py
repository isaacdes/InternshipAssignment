from django.shortcuts import render
from django.http import HttpResponse
from Submission.models import Details
# from .models import Details

# Create your views here.

def homepage(request):
    if request.method == 'POST' and 'bt1' in request.POST:
        name = request.POST['nm']
        email = request.POST['em']
        phno = request.POST['phno']

        obj =  Details(name=name, email=email, phno=phno)
        obj.save()

        print("The data has been uploaded")
        

    # return HttpResponse("Welcome to Sherry Technnologies")
    return render(request, 'home.html')

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']

        obj =  Details(name=name, email=email, phno=phno)
        obj.save()

        print("The data has been uploaded")

        return HttpResponse('')