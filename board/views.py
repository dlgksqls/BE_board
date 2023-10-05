from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def create_view(request):
    if request.method == "GET":
        return render(request, "board/board_create.html")
