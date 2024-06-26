#forms.py
from multiupload.fields import MultiFileField
from django import forms
from .models import UploadedFile
from mysite.models import UploadedFile
from django.core.validators import FileExtensionValidator



class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']  # Поля формы, которые необходимо включить
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]


class AnalysisResultsForm(forms.Form):
    results = forms.CharField(widget=forms.Textarea)

