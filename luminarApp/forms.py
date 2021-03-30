
from django import forms
from .models import *
from django.forms import ModelForm,Textarea,TextInput

class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class BatchCreateForm(ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'
        widgets = {
            'batch_code': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_date': forms.TextInput(attrs={'class': 'form-control'}),
            'course_fees': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_status': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def clean(self):
            print("hellp")