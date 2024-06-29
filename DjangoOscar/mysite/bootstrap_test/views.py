# views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from mysite.forms import FileUploadForm, FileEditForm, UserRegisterForm  # Импорт обеих форм
from mysite.models import XMLSchema, UploadedFile

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.db.models.functions import TruncDay
from django.contrib import messages

from django.template.loader import render_to_string
from mysite.models import UserProfile
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Count

from django.views.decorators.http import require_POST

import json
import logging


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


def user_uploads(request):
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'profile/user_uploads.html', {'uploaded_files': uploaded_files})


def edit_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    if request.method == 'POST':
        form = FileEditForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return redirect('user_uploads')
    else:
        form = FileEditForm(instance=file)
    return render(request, 'redact_form.html', {'form': form, 'file': file})  # Передаем объект file в контексте


@require_POST
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    file.delete()
    return JsonResponse({'success': True})






# Обработка профиля

@login_required
def profile(request):
    # Получаем текущего пользователя
    user = request.user
    users = User.objects.all()  # Получаем всех пользователей
    schemas = XMLSchema.objects.all()

    # Получаем загруженные файлы текущего пользователя
    uploaded_files = UploadedFile.objects.filter(uploaded_by=user)

    # Передаем данные в шаблон 'user_profile.html'
    context = {
        'user': user,
        'users': users,
        'uploaded_files': uploaded_files,  # Передаем список загруженных файлов текущего пользователя
        'schemas': schemas,
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

def admin_users(request):
    users = User.objects.all().select_related('userprofile')
    return render(request, 'profile/admin_users.html', {'users': users})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт {username} был успешно создан! Вы можете войти в систему.')
            login(request, user)  # Автоматический вход после регистрации
            return redirect('profile')
        else:
            messages.error(request, 'Ошибка при регистрации. Пожалуйста, попробуйте снова.')
    else:
        form = UserRegisterForm()
    return render(request, 'user_register.html', {'form': form})



@login_required
def user_statistic(request):
    user = request.user
    total_files = UploadedFile.objects.filter(uploaded_by=user).count()

    context = {
        'total_files': total_files,
        'user': user,
    }
    return render(request, 'user_profile.html', context)