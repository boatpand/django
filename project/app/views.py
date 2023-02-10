from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Person
from django.contrib import messages

# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Response !!!</h1>')
def index(request):
    # name = "Admin"
    # age = 22
    # return render(request,"index.htm",{"name":name, "age":age})
    
    # all_person = Person.objects.all()
    all_person = Person.objects.filter(age=15)
    return render(request,"index.htm",{"all_person":all_person})

def about(request):
    return render(request,"about.htm")

def form(request):
    if request.method == "POST":
        # recieve data
        name = request.POST["name"]
        age = request.POST["age"]
        # save data
        person = Person.objects.create(
            name = name,
            age = age
        )
        person.save()
        messages.success(request, "Success!!")
        return redirect("/")
    else:
        return render(request,"form.htm")

def edit(request, person_id):
    # case Edit data in /edit
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "Update Success!!")
        return redirect("/")
    # case press Edit button
    else:
        person = Person.objects.get(id=person_id)
        return render(request,"edit.htm",{"person":person})

def delete(request, person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request, "Delete Success!!")
    return redirect("/")