from .models import *
from django.forms import ModelForm
class e(ModelForm):
    class Meta:
        model=Register
        fields="__all__"