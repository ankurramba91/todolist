from django.shortcuts import render
from home.models import Tasks

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method =="POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Tasks(tasktitle=title,taskdesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context) 

def tasks(request):
    allTasks = Tasks.objects.all()
    context = {'tasks': allTasks}
    return render(request,'tasks.html',context)