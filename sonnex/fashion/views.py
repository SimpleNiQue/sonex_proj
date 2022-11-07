from django.shortcuts import render

def home(request):
    template = "fashion/index.html"
    context = dict()

    return render(request, template)
