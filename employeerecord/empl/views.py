from django.shortcuts import render, redirect

# Create your views here.
from .models import Employee
from .forms import EmployeeForm


def all_employees(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'emp/index.html', context)


from django.contrib import messages


def add_employees(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"Employee {form.cleaned_data.get('name')} has been added")
        return redirect('allEmp')

    context = {
        'form': form,
    }
    return render(request, 'emp/addEmp.html', context)


def edit_employees(request, id=None):
    one_emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=one_emp)
    if form.is_valid():
        form.save()

        messages.add_message(request, messages.INFO, f"{form.cleaned_data.get('name')} has been added")
        return redirect('allEmp')

    context = {
        'form': form,
    }
    return render(request, 'emp/editEmp.html', context)


def one_employee(request, id=None):
    emp = Employee.objects.get(id=id)
    context = {
        'emp': emp
    }
    return render(request, 'emp/viewEmp.html', context)


def delete_employee(request, id=None):
    emp = Employee.objects.get(id=id)
    if request.method == "POST":
        emp.delete()
        messages.add_message(request, messages.INFO, f"{emp.name} Employee Deleted")
        return redirect('allEmp')
    context = {
        'emp': emp
    }
    return render(request, 'emp/delete.html', context)
