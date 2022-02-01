from django.http import Http404
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


def search_results(request):
    try:
        if 'picture' in request.GET and request.GET["picture"]:
            search_term = request.GET.get("picture")
            searched_images = Image.search_by_category(search_term)
            message = f'{search_term}'
            return render(request, "search_results.html", {"message": message, "pictures": searched_images})
        else:
            message = "You haven't searched for any term"
            return render(request, "search_results.html", {"message": message})
    except Image.DoesNotExist:
        raise Http404
    