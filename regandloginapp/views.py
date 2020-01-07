from django.shortcuts import render

from  regandloginapp.models import registrationdata
from regandloginapp.forms import *
from django.http.response import HttpResponse
# def index(request):
#     return render(request,'indexfile.html')


def registration_view(request):
    if request.method=='POST':
        rform=registrationform(request.POST)
        if rform.is_valid():
            fname=request.POST.get("firstname")
            lname=request.POST.get("lastname")
            uname=request.POST.get("username")
            pword=request.POST.get("password")
            mobile=request.POST.get("mobile")
            email=request.POST.get("email")
            gender=rform.cleaned_data.get("gender")
            dob=rform.cleaned_data.get("date_of_birth")
            data=registrationdata(
                firstname=fname,
                lastname=lname,
                username=uname,
                password=pword,
                mobile=mobile,
                email=email,
                gender=gender,
                date_of_birth=dob
            )
            data.save()
            rform = registrationform()
            return render(request, 'registration.html', {'rform': rform})

        else:
            return HttpResponse(" enter all values")



    else:
        rform=registrationform()
        return render(request,'registration.html',{'rform':rform})


def loginview(request):
    if request.method=='POST':
        lform=loginform(request.POST)
        if lform.is_valid():
           uname= request.POST.get("username")
           pword=request.POST.get("password")
           uname1=registrationdata.objects.filter(username=uname)
           pword1=registrationdata.objects.filter(password=pword)
           if uname1 and pword1:
               return HttpResponse('LOGIN SUCCESSFULLY')
           else:
               return HttpResponse('login failed')

        else:
            return HttpResponse('INVALID CREDENTIALS')
    else:
        lform=loginform()
        return render(request,'login.html',{'lform':lform})
