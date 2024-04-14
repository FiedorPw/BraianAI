from django import forms
from .models import FileModel


# dodane dodawanie plików
# class FileUploadForm(forms.Form):  # Note: Using forms.Form as there's no specific model to associate with
#     file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['file']



