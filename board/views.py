from django.shortcuts import render, redirect
from .models import Board

# Create your views here.


def home(request):
    return render(request, "home.html")


def create_view(request):
    if request.method == "GET":
        return render(request, "board/board_create.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.POST.get("image")

        board = Board(title=title, contents=content, images=image)
        board.writer = request.user

        board.save()

        return redirect("board:home")


def detail_view(request, id):
    try:
        board = Board.objects.get(id=id)
    except Board.DoesNotExist:
        return redirect("board:home")

    context = {
        "board": board,
    }

    return render(request, "board/board_detail.html", context)


def update_view(request, id):
    board = Board.objects.get(id=id)  # 선택한 데이터 조회
    if request.method == "GET":
        context = {"board": board}
        return render(request, "board/board_update.html", context)
    elif request.method == "POST":
        new_image = request.POST.get("image")
        content = request.POST.get("content")

        if new_image:
            board.images.delete()
            board.images = new_image
        board.contents = content
        board.save()

        return redirect("board:home")
