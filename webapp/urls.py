from django.urls import path
from webapp import views

urlpatterns=[
    path('home_page/',views.home_page,name="home_page"),
    path('about_page/',views.about_page,name="about_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('popular_books/',views.popular_books,name="popular_books"),
    path('filtered_books/<book_category>/',views.filtered_books,name="filtered_books"),
    path('single_book/<int:book_id>/',views.single_book,name="single_book"),
    path('signup_page/',views.signup_page,name="signup_page"),
    path('signin_page/',views.signin_page,name="signin_page"),
    path('user_signup/',views.user_signup,name="user_signup"),
    path('user_login/',views.user_login,name="user_login"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),


]