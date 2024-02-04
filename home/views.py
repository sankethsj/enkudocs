from django.shortcuts import render

# Create your views here.
def index(request):
    name = "Sanketh"
    context = {
        "name": name
    }
    return render(request, "home/index.html", context=context)