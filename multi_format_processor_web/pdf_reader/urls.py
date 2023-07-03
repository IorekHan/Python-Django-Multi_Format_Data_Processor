from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.read_pdf_home, name='read_pdf_home'),
    path('logout/', views.logout, name='logout'),
    path('home/pdf_read', views.read_pdf_storage, name='read_pdf'),
    path('home/filestorage/download/<filename>', views.read_pdf_downloadfile, name='read_pdf_download'),
    path('home/filestorage/delete/<filename>', views.read_pdf_deletefile, name='read_pdf_delete'),
]