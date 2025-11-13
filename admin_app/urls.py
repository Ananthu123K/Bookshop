from django.urls import path
from admin_app import views

urlpatterns=[
    path('Home/',views.index_page,name="Home"),
    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('update_category/<int:cat_id>/', views.update_category, name='update_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('add_book/', views.add_book, name="add_book"),
    path('display_book/',views.display_book,name="display_book"),
    path('save_book/',views.save_book,name="save_book"),
    path('edit_book/<int:book_id>/',views.edit_book,name="edit_book"),
    path('update_book/<int:b_id>/',views.update_book,name="update_book"),
    path('delete_book/<int:b_id>/',views.delete_book,name="delete_book"),
    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('display_message/',views.display_message,name="display_message"),
    path('delete_message/<int:m_id>/',views.delete_message,name="delete_message"),

]