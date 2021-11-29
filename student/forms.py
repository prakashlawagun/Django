from django.forms import ModelForm
from .models import Student

class StudendForm(ModelForm):
    class Meta:
        model = Student
        fields = ['frist_name','last_name','email']
