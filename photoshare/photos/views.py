from django.db.models import query
from django.http import request
from django.shortcuts import render, redirect
from .models import Category, Photo
import os
from fnmatch import fnmatch

# Create your views here.


def listaPastas(request):
    categories = Category.objects.all()

    root = "/home/arthur/repos/tmp/most-will/Mostruario/"
    pattern = "*.jpg"
    listCategorias = []
    listImagens = []
    data = request.POST

    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                # Crindo o nome da categoria
                novaCategoria = path.replace(root, "")
                # Localização da fotos
                caminhoImagem = path + "/" + name
                category, created = Category.objects.get_or_create(name=novaCategoria)
                # Passando a categoria e a lista de imagens para o template
                # addPhoto(request,novaCategoria,caminhoImagem)


def gallery(request):
    category = request.GET.get("category")
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    listaPastas(request)
    categories = Category.objects.all()
    context = {"categories": categories, "photos": photos}
    return render(request, "photos/gallery.html", context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, "photos/photo.html", {"photo": photo})


def addPhoto(request):
    categories = Category.objects.all()
    categoria = request.GET.get("categoria")
    fotoAtual = request.GET.get("fotoAtual")

    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist("images")

        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(
                name=data["category_new"]
            )
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data["description"],
                image=image,
            )
        return redirect("gallery")

    context = {"categories": categories}
    return render(request, "photos/add.html", context)


# python manage.py runserver 7000
# python manage.py makemigrations
# python manage.py migrate
# python manage.py collectstatic
