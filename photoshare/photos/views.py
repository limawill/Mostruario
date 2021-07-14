from django.http import request
from django.shortcuts import render, redirect
from .models import Category, Photo
import os 
from fnmatch import fnmatch

# Create your views here.

def listaPastas(request):
    categories = Category.objects.all()

    root='/home/will/Imagens/Mostruario/'
    pattern = ("*.jpg")
    listCategorias = []
    listImagens = []
    
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
            # Removendo o caminho inteiro
                listCategorias.append(path.replace(root,""))  
                listImagens.append(path+name)
                # Localização da fotos
                #s2 = path+name
                #print(s2)/
    listCategorias = sorted(set(listCategorias))

    print ("Antes do for:")
    for i in listCategorias:
        print ("Valor de i:", i)
        #posts = Post.
        #if request.method == 'POST':
        #data = request.POST
        #category, created = Category.objects.get_or_create(i)
    category, created = request.POST.getlist(listCategorias)
    #return redirect('gallery')

    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)



def gallery(request):
    
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name= category)

    print ('Passou aqui?')
    listaPastas(request)
    print ('Passou aqui 2 ?')

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})




def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)



#python manage.py runserver 7000
#python manage.py makemigrations
#python manage.py migrate
#python manage.py collectstatic


