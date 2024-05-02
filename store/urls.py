from django.urls import path
from . import views

urlpatterns = [
    #The path takes in three areas namely;
    #The first area is for then name to be showned in the url path
    #The second area is the method or function created in the views.py file where all the action are wrtiien in particular to the creation of the method of function
    #The third area has an attribute called name which is to be used in accessing our file when navigation and it is needed in out template/html files 
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('search/', views.search, name='search'),
]
