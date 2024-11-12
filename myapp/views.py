from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now()
    isActive = True  # Default state
    
    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)  # Debugging check, ensure it's intended for debugging
        isActive = check is not None  # Set isActive based on the check variable

    name = "Dawa"
    
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    
    student = {
        "student_name": "Rahul",
        "student_college": "ZYZ",  
        "student_city": "LUCKNOW"
    }

    data = {
        "date": date,
        "isActive": isActive,
        "name": name,
        "list_of_programs": list_of_programs,
        "student_data": student
    }

    return render(request, "home.html", data)  

def about(request):
    return render(request, "about.html", {})

def service(request):
    return render(request, "service.html", {})
