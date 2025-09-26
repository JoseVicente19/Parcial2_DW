from django import forms
from .models import Videos

class VideosForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = '__all__'