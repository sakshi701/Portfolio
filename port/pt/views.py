from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, 'home.html')