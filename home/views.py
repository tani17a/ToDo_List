from django.shortcuts import render,HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    contex={'success':False,'Name':'Hello'}
    if request.method=="POST":
        title=request.POST['title']
        disc=request.POST.get('desc',False)
        instant=Task(Tittle=title,Description=disc)
        instant.save()
        contex={'success':True }
    return render(request,'home.html',contex)
       
def task(request):
    alltasks=Task.objects.all()
    contex={'tasks':alltasks}
    return render(request,'task.html',contex)
