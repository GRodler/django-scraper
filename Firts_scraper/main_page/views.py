from django.contrib import messages
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect

from .forms import AgeForm
from .models import User_info
# Create your views here.
def home(request):
    return render(request,'index.html')

def saveData(form):
    form = form.cleaned_data  # return a dictionary with the data in normal python types
    d = User_info(name=form['name'],age=form['age'],extra=form['info'])
    d.save()#django does not touch the database until you call the save method

def check_if_exist(form):#checks if there alredy is someone with the same name
    found = False

    if User_info.objects.exists():
        query = User_info.objects.values()
        form = form.cleaned_data
        names = [entry for entry in query]
        for name in names:
            if form['name'] == name['name']:
                found = True
    return found

def take_info(request):#while im in this page this view generate an empty form to show if im not calling the post method
    #the request seems helpful in many cases

    if request.method == 'POST':
        form = AgeForm(request.POST) #puts all the fields in a istance of the class form
        if form.is_valid():#uses a built in method tho check if is a valid for
            if not check_if_exist(form):
                saveData(form)
                return HttpResponseRedirect('../resume')#i redirect to the home page
            else:
                messages.error(request,'seems that this name alredy gave some info')
    else:
        form = AgeForm()
    return render(request, 'information/little_form.html', {'form':form})
def give_info(request):
    query = User_info.objects.all()#values takes the value and convert into a dict
    return render(request,'information/info.html', {'query': query},)