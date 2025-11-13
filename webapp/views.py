from django.shortcuts import render,redirect
from admin_app.models import CategoryDb,BookDb
from .models import RegistrationDb,ContactDb

# Create your views here.
def home_page(request):
    category =CategoryDb.objects.all()
    books = BookDb.objects.all()
    return render(request, 'Home.html', {'category':category,"books":books})
def about_page(request):
    category = CategoryDb.objects.all()
    return render(request,"About.html",{'category':category})

def contact_page(request):
    category = CategoryDb.objects.all()
    return render(request,"Contact.html",{'category':category})

def popular_books(request):
    category = CategoryDb.objects.all()
    books=BookDb.objects.all()
    return render(request,"Popular_books.html",{'category':category,"books":books})

def filtered_books(request,book_category):
    category = CategoryDb.objects.all()
    books=BookDb.objects.filter(Category=book_category)
    return render(request,"Filtered_books.html",{"books":books,"category":category})

def single_book(request,book_id):
    category = CategoryDb.objects.all()
    books=BookDb.objects.get(id=book_id)
    return render(request, "Single_book.html", {"books": books,"category":category})
def signin_page(request):
    return render(request,"Signin_page.html")
def signup_page(request):
    return render(request,"Signup_page.html")




def user_signup(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone = request.POST.get('phone')
        password = request.POST.get('Password')
        confirm_password = request.POST.get('Confirm_password')

        # Check if user already exists
        if RegistrationDb.objects.filter(Email=email).exists():
            # print("Email already exists") using js alert message
            return redirect('signup_page')
        elif RegistrationDb.objects.filter(Name=name).exists():
            # print("Username already exists")using js alert message
            return redirect('signup_page')
        elif password != confirm_password:
            # print("Passwords do not match") using js alert message
            return redirect('signup_page')
        else:
            user = RegistrationDb(
                Name=name,
                Email=email,
                phone=phone,
                Password=password,
                Confirm_password=confirm_password,
            )
            user.save()
            print("User created successfully")
            return redirect('signin_page')

    return render(request, 'signup.html')
#user signin

def user_login(request):
    if request.method == 'POST':
        un= request.POST.get('username')
        pswd = request.POST.get('password')

        # Check credentials
        user = RegistrationDb.objects.filter(Name=un, Password=pswd).exists()

        if user:
            # Create session
            request.session['Name'] = un
            request.session['Password'] = pswd
            return redirect('home_page')
        else:
            print("Invalid credentials")
            return redirect('signin_page')
    else:
        return redirect('signin_page')

#delete session
def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(user_login)


#contact view
def save_contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        obj=ContactDb(User_name=name,User_email=email,Subject=subject,Message=message)
        obj.save()
        return redirect(contact_page)

def cart_page(request):
    return render(request,"Cart.html")

def checkout_page(request):
    return render(request,"Checkout_page.html")





