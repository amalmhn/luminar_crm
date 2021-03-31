
from django import forms
from .models import *
from django.forms import ModelForm,Textarea,TextInput,SelectMultiple

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
            'course': forms.Select(attrs={'class': 'form-control'}),
            'batch_date': forms.TextInput(attrs={'class': 'form-control'}),
            'course_fees': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_status': forms.Select(attrs={'class': 'form-control'}),
        }

class EnquiryCreateForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        widgets = {
            'enquiryId': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'collegename': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'enquirydate': forms.TextInput(attrs={'class': 'form-control'}),
            'followup_date': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }
