from django.shortcuts import render,redirect
from . models import Todo


# Create your views here.
def home(request):
    if request.method == 'POST':
        sl_no=request.POST.get('sl_no')
        items_name=request.POST.get('items_name')
        description=request.POST.get('description')
        task=Todo(sl_no=sl_no,items_name=items_name,description=description)
        task.save()
    task1=Todo.objects.all()    
    return render(request,"index.html",{'task':task1})

def delete(request,taskid):
    task=Todo.objects.get(id=taskid)
    task.delete()
    return redirect('/')
    
def update(request, id):
    contact1 = Todo.objects.all()
    contact = Todo.objects.get(id=id)

    if request.method == 'POST':
        slno = request.POST.get('sl_no', '')
        itemname = request.POST.get('items_name', '')
        description = request.POST.get('description', '')

        contact.sl_no = slno
        contact.items_name = itemname
        contact.description = description
        contact.save()

        return redirect('/')

    return render(request, 'update.html', {'contact1': contact1, 'contact': contact})  