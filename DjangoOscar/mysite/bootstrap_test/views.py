# views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from mysite.forms import FileUploadForm  # Импорт обеих форм
from mysite.models import XMLSchema, UploadedFile
from django.db.models import Count
from django.db.models.functions import TruncDay

from django.template.loader import render_to_string
from mysite.models import UserProfile
from django.utils import timezone

import json


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
def upload_file(request):
    if request.method == 'POST':
        if 'fileInput' in request.FILES:
            uploaded_file = request.FILES['fileInput']
            if uploaded_file.name.endswith('.pdf'):
                uploaded_instance = UploadedFile(
                    uploaded_by=request.user,
                    name=uploaded_file.name,
                    file=uploaded_file
                )
                uploaded_instance.save()
                latest_file = uploaded_instance
                return render(request, 'redact_form.html', {'latest_file': latest_file})
            else:
                form = FileUploadForm()
                return render(request, 'upload.html', {'form': form, 'error': 'Только PDF файлы разрешены.'})
        else:
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = form.save(commit=False)
                uploaded_file.uploaded_by = request.user
                uploaded_file.name = uploaded_file.file.name
                uploaded_file.save()
                latest_file = UploadedFile.objects.filter(uploaded_by=request.user, file__endswith='.pdf').last()
                return render(request, 'redact_form.html', {'latest_file': latest_file})
    else:
        form = FileUploadForm()
    
    return render(request, 'upload.html', {'form': form})



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








# Обработка профиля

@login_required
def profile(request):
    # Получаем текущего пользователя
    user = request.user
    
    # Получаем загруженные файлы текущего пользователя
    uploaded_files = UploadedFile.objects.filter(uploaded_by=user)

    # Передаем данные в шаблон 'user_profile.html'
    context = {
        'user': user,
        'uploaded_files': uploaded_files,  # Передаем список загруженных файлов текущего пользователя
    }
    return render(request, 'user_profile.html', context)
#    return render(request, 'profile/user_uploads.html', context)

    



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
    

def user_profile_view(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'user_profile.html', {'user_profiles': user_profiles})



@login_required
def user_statistic(request):
    user = request.user
    
    # Общее количество файлов
    total_files = UploadedFile.objects.filter(uploaded_by=user).count()

    # Файлы, загруженные сегодня
    start_of_today = now().replace(hour=0, minute=0, second=0, microsecond=0)
    files_today = UploadedFile.objects.filter(uploaded_by=user, uploaded_at__gte=start_of_today).count()

    # Файлы, загруженные в этом месяце
    start_of_month = now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    files_this_month = UploadedFile.objects.filter(uploaded_by=user, uploaded_at__gte=start_of_month).count()

    # Файлы, загруженные в этом году
    start_of_year = now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    files_this_year = UploadedFile.objects.filter(uploaded_by=user, uploaded_at__gte=start_of_year).count()

    # Отладочный вывод
    print(f"User: {user.username}, Total files: {total_files}, Files today: {files_today}, Files this month: {files_this_month}, Files this year: {files_this_year}")

    context = {
        'total_files': total_files,
        'files_today': files_today,
        'files_this_month': files_this_month,
        'files_this_year': files_this_year,
    }
    
    return render(request, 'user_profile.html', {'total_files': total_files})
