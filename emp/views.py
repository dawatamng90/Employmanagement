from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp,Testimonial
from .form import FeedbackForm

def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "emp/home.html", {
        "emps": emps
    })

def add_emp(request):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        
        e = Emp(
            name=emp_name,
            emp_id=emp_id,
            phone=emp_phone,
            address=emp_address,
            department=emp_department,
            working=bool(emp_working),
        )
        e.save()
        
        return redirect("/emp/home/")
    return render(request, "emp/add_emp.html", {})

def delete_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    return render(request, "emp/update_emp.html", {
        "emp": emp
    })

def do_update_emp(request, emp_id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        
        e = Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        e.working = bool(emp_working)
        e.save()
        
    return redirect("/emp/home/")

def testimonials(request):
    testi = Testimonial.objects.all()
    return render(request, "emp/testimonials.html",{
        'testi':testi
    })
    
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)  # Corrected request.post to request.POST
        if form.is_valid():
            # Process form data here since it's a regular Form, not ModelForm
            # For example, you might manually save data if FeedbackForm isn't bound to a model
            print(form.cleaned_data)  # For debugging or to process data
            # Redirect or render a success message
            return redirect("/emp/feedback/")
        else:
            return render(request, "emp/feedback.html", {'form': form})
    else:
        form = FeedbackForm()
    return render(request, "emp/feedback.html", {'form': form})