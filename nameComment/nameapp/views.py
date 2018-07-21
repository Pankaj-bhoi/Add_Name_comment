from django.shortcuts import render
from nameapp .form import PersonForm
from nameapp . models import Person
from django.http import HttpResponse,HttpResponseRedirect

def makeentry(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            desc = request.POST.get('Comment','')
            person =Person(name=name,desc=desc)
            person.save()
            return HttpResponse("<h1 align='center'>Your comment has been added</h1>")

            form = PersonForm()
            return render(request,'makeentry.html',{'form':form})
    else:
        form = PersonForm()
        return render(request,'makeentry.html',{'form':form})
