from django.shortcuts import render

def homepage(request):
    return render(request,"homepage.html")

def about(request):
    return render(request,"about.html")

def people(request):
    return render(request,"people.html")


def ach(request):
    return render(request,"ach.html")
