from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import About

def about_view(request):
    about = get_object_or_404(About)
    return render(request, "about/about.html", {"about": about})
