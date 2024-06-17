from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from mysite.forms import FileUploadForm
from mysite.models import XMLSchema, UploadedFile

def get_schemas(request):
    schemas = XMLSchema.get_schema_choices()
    return JsonResponse({'schemas': list(schemas)})

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def gallery(request):
    return render(request, "gallery.html")

def pricing(request):
    return render(request, "pricing.html")

def contact(request):
    return render(request, "contact.html")

@login_required
def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.uploaded_by = request.user
            uploaded_file.save()
            print("File uploaded successfully:", uploaded_file.file.name)
            return redirect('redact_form')
    else:
        form = FileUploadForm()
    
    schemas = XMLSchema.get_schema_choices()
    return render(request, 'upload.html', {'form': form, 'schemas': schemas})

@login_required
def redact_form(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            # Ваш код обработки PDF-файла здесь
            print("PDF file uploaded successfully:", uploaded_file.name)
            
    else:
        form = FileUploadForm()
    
    return render(request, 'redact_form.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user_profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            error_message = "Неверное имя пользователя или пароль."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')