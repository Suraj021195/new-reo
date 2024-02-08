from django.shortcuts import render,redirect
from .models import employee,desingations
from .forms import employeeForm


# Create your views here.

def dashboard(request):
    return render(request,"index.html")


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
    data =employee.objects.all().order_by('-created')
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
        

# def delete(request,id):
#     gatedata=employee.objects.get(id=id)
#     gatedata.delete()
#     return request(request,'Delete_employee',{'gatedata': gatedata})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        form = employee.objects.get(id=id)
        form.delete()
        return redirect('viewlist')  # Redirect to some URL after deletion
    else:
      form= employee.objects.all()
      return render(request, 'delete_employee.html', {'form': form})
