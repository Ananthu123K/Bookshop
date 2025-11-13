import datetime

from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from admin_app.models import CategoryDb, BookDb
from webapp.models import ContactDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index_page(request):
    categories=CategoryDb.objects.count()
    book=BookDb.objects.count()
    date=datetime.datetime.now()
    return render(request,"index.html",{"categories":categories,"book":book,"date":date})


def add_category(request):
    return render(request,"Add_category.html")
def save_category(request):
    if request.method=="POST":
        category_name=request.POST.get('category_name')
        description=request.POST.get('Description')
        cover_image=request.FILES['Cover_Image']

        obj=CategoryDb(
            Category_name=category_name,
            Description=description,
            Cover_Image=cover_image

        )
        obj.save()
        return redirect(add_category)
def display_category(request):
    category=CategoryDb.objects.all()
    return render(request,"Display_category.html",{"category":category})
def edit_category(request,category_id):
    category=CategoryDb.objects.get(id=category_id)
    return render(request,"Edit_category.html",{"category":category})



def update_category(request,cat_id):
    if request.method=="POST":
        category_name = request.POST.get('category_name')
        description = request.POST.get('Description')

        try:
            img=request.FILES['Cover_Image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDb.objects.get(id=cat_id).Cover_Image
        CategoryDb.objects.filter(id=cat_id).update(
            Category_name=category_name,
            Description=description,
            Cover_Image=file

        )
        return redirect(display_category)

def delete_category(request, category_id):
    category = CategoryDb.objects.get(id=category_id)
    category.delete()
    return redirect('display_category')


#Book view
def add_book(request):
    categories=CategoryDb.objects.all()
    return  render(request,"Add_book.html",{"categories":categories})


def display_book(request):
    books= BookDb.objects.all()
    return render(request,"Display_book.html",{"books":books})
def save_book(request):
    if request.method=="POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        category= request.POST.get('category')
        price = request.POST.get('price')
        publisher = request.POST.get('publisher')
        description = request.POST.get('description')
        cover_image= request.FILES['cover_image']

        obj=BookDb(
            Title=title,
            Author=author,
            Category=category,
            Price=price,
            Publisher=publisher,
            Description=description,
            Cover_image=cover_image
        )
        obj.save()
        return redirect(add_book)

def edit_book(request, book_id):
    book = BookDb.objects.get(id=book_id)
    categories = CategoryDb.objects.all()
    return render(request, "Edit_book.html", {"book": book, "categories": categories})

def update_book(request, b_id):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        price = request.POST.get('price')
        publisher = request.POST.get('publisher')
        description = request.POST.get('description')

        try:
            # if a new image is uploaded
            img = request.FILES['cover_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            # if no new image is uploaded, keep the old one
            file = BookDb.objects.get(id=b_id).Cover_image

        # update book details
        BookDb.objects.filter(id=b_id).update(
            Title=title,
            Author=author,
            Category=category,
            Price=price,
            Publisher=publisher,
            Description=description,
            Cover_image=file
        )

        return redirect('display_book')

def delete_book(request,b_id):
    data=BookDb.objects.get(id=b_id)
    data.delete()
    return redirect(display_book)


def admin_login_page(request):
    return render(request,"Admin_login.html")
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            data=authenticate(username=un,password=pswd)
            if data is not None:
                login(request,data)
                request.session['username']=un
                request.session['password']=pswd
                return redirect(index_page)
            else:
                return redirect(admin_login_page)
        else:
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

def display_message(request):
    messages=ContactDb.objects.all()
    return render(request,"Display_messages.html",{"messages":messages})

def delete_message(request,m_id):
    data=ContactDb.objects.get(id=m_id)
    data.delete()
    return redirect(display_message)





