from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from functools import wraps
from django.http import Http404
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

from .forms import FileUploadForm

# include compliance user DB
from pdf_reader.models import storageUser


def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        
        ret = request.session.get("login")

        if ret == "success":
            return func(request, *args, **kwargs)
        
        else:
            next_url = request.path_info
            return redirect("/pdf_read/login/?next={}".format(next_url))
    return inner

def login(request):
    if request.method == "POST":
        input_username = request.POST.get("user")
        input_password = request.POST.get("pwd")
        
        next_url = request.GET.get("next")
        
        stored_user =  storageUser.objects.filter(username = input_username).first()
        
        if stored_user:
        
            stored_password = stored_user.password
            stored_name = stored_user.name
            stored_email = stored_user.email
            
            if input_password == stored_password:
                if next_url:
                    rep = redirect(next_url)
                else:
                    rep = redirect("/pdf_read/home/")
 
                request.session["login"] = "success"
                request.session["name"] = stored_name
                request.session["email"] = stored_email
        
                request.session.set_expiry(600)
            
                return rep
            
    ret = request.session.get("login")
    
    if ret == "success":
        return redirect("/pdf_read/home/")
    else:
        return render(request, "pdf_read/login.html")
    


@check_login
def read_pdf_home(request):
    name = request.session.get("name")

    return render(request, "read_pdf/home.html", {"name": name})

@check_login
def read_pdf_storage(request):
    name = request.session.get("name")
    
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, settings.MEDIA_PDFREAD))
        if form.is_valid():
            files = request.FILES.getlist('files')
            # operations on uploaded files
            for file in files:
                filename = fs.save(file.name, file)
                uploaded_file_url = fs.url(filename)
        files = fs.listdir('')

    else:
        form = FileUploadForm()
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, settings.MEDIA_MEDIA_PDFREAD))
        files = fs.listdir('')
    return render(request, "read_pdf/filestorage.html", {'form': form, 
                                                                'files': files[1],
                                                                "name": name, 
                                                                })

@check_login
def read_pdf_deletefile(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, settings.MEDIA_PDFREAD, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return redirect('read_pdf_home')
    else:
        raise Http404
        
@check_login
def read_pdf_downloadfile(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, settings.MEDIA_PDFREAD, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        raise Http404
    

def logout(request):
    request.session.flush()
    request.session.delete()
    return render(request, "read_pdf/logout.html")