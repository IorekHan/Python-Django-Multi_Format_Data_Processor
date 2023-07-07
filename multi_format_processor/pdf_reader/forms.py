from django import forms
from django.forms.widgets import ClearableFileInput, CheckboxInput, FileInput

class MultipleFileInput(FileInput):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.attrs['multiple'] = True

class FileUploadForm(forms.Form):
    files = forms.FileField(widget=MultipleFileInput)
