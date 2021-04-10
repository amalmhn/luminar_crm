
from django import forms
from .models import *
from django.forms import ModelForm,Textarea,TextInput,SelectMultiple
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
        model = EnquiryThree
        fields = '__all__'

class AdmissionCreateForm(ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'

class PaymentCreateForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class RegistrationForm(UserCreationForm):
  class Meta:
      model = User
      fields = ['username', 'password1', 'password2','first_name','last_name','email']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=130)






