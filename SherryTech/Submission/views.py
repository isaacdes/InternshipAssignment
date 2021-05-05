from django.shortcuts import render
from django.http import HttpResponse
from Submission.models import Details
# from .models import Details

# Create your views here.

def homepage(request):
    if request.method == 'POST':
        name = request.POST['nm']
        email = request.POST['em']
        phno = request.POST['phno']

        obj =  Details(name=name, email=email, phno=phno)
        obj.save()

        # obj = Details()
        # obj.name = name
        # obj.email = email
        # obj.phno =  phno
        # obj.save()
    

        print("The data has been uploaded")
        

    # return HttpResponse("Welcome to Sherry Technnologies")
    return render(request, 'home.html')

    