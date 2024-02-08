from django.shortcuts import render,redirect
from .models import employee,desingations
from .forms import employeeForm


# Create your views here.
def employeedetails(request):
    if request.method =="POST":
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewlist')
    else:
        form=employeeForm()
    return render(request,'Add_employee.html',{'form':form})

def viewlist(request):
    data =employee.objects.all().order_by('first_name')
    return render(request,"Employee_list.html",{'data':data})

def edit(request,id):
    getdata=employee.objects.get(id=id)
    if request.method=="POST":
        form=employeeForm(request.POST,instance=getdata)
        if form.is_valid():
            form.save()
            return redirect('viewlist')
    else:
        form=employeeForm(instance=getdata)
    return render(request,'Add_employee.html',{'form':form})
        
        