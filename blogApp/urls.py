from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('author/<name>', views.getauthor, name="author"),
    path('article/<int:id>', views.getsingle, name="single-post"),
    path('topic/<name>', views.getTopic, name="topic"),
    path('login', views.getLogin, name="login"),
    path('logout', views.getLogout, name="logout"),
    path('create', views.getCreate, name="create"),
    path('profile', views.getProfile, name="profile"),
    path('update/<int:pid>', views.getUpdate, name="update"),
    path('delete/<int:pid>', views.getDelete, name="delete"),
    path('register', views.getRegister, name="register"),
    path('category', views.getCategory, name="category"),
    path('category-add', views.categoryAdd, name="category-add"),
    path('category-update/<int:id>', views.categoryUpdate, name="category-update"),
    path('category-delete/<int:id>', views.categoryDelete, name="category-delete"),

]
