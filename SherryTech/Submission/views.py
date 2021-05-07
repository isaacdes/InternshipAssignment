from django.shortcuts import render
from django.http import HttpResponse
from Submission.models import Details

import re
# for validating an Email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


# Create your views here.

def homepage(request):
    if request.method == 'POST' and 'bt1' in request.POST:
        name = request.POST['nm']
        email = request.POST['em']
        phno = request.POST['phno']

        # error_msg = ""
        # if(not re.search(regex,email)):
        #     error_msg ="Enter proper email"

        # if not error_msg:
           
            
        # else:
        #     return render(request, 'home.html', {'error': error_msg})
        obj =  Details(name=name, email=email, phno=phno)
        obj.save()

        print(name + " " + email + " " + phno + " Submit1")
        print("The data has been uploaded")
    return render(request, 'home.html')        


    
def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']

        obj =  Details(name=name, email=email, phno=phno)
        obj.save()

        print(name + " " + email + " " + phno + " Ajax Submit")
        print("The data has been uploaded")

        return HttpResponse('')

def display(request):

    return render(request, "display.html")
    # return HttpResponse("displaying data")