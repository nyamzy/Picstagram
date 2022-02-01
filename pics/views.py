from django.shortcuts import render, redirect
from .models import Image

# Create your views here.
def welcome(request):
    title = "Home"
    image_list = Image.objects.all()
    context = {
        "title": title,
        "image_list": image_list
    }
    return render(request, "welcome.html", context)