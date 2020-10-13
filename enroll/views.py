from django.shortcuts import render,redirect
from .forms import StudentRegistration
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/addandshow.html',{'form':fm})
    