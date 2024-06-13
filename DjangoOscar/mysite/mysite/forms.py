#forms.py
from multiupload.fields import MultiFileField
from django import forms
from .models import UploadedFile


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['name', 'file']


class AnalysisResultsForm(forms.Form):
    results = forms.CharField(widget=forms.Textarea)








