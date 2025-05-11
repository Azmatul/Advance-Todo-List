from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, "login_page.html")

def registration_page(request):
    return render(request, "registration_page.html")