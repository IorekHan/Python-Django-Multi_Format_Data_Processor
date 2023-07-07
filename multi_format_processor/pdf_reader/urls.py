from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.read_pdf_home, name='read_pdf_home'),
    path('home/runtxt', views.convert_txt, name='pdf_txt'),
    path('home/runword', views.convert_word, name='pdf_word'),
    path('logout/', views.logout, name='logout'),
    path('home/download/<filename>', views.read_pdf_downloadfile, name='read_pdf_download'),
    path('home/delete/<filename>', views.read_pdf_deletefile, name='read_pdf_delete'),
]