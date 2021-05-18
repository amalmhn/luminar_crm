
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
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_duration': forms.TextInput(attrs={'class': 'form-control'}),

        }

class BatchCreateForm(ModelForm):
    class Meta:
        model = BatchModelNew
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
        widgets = {
            'enquiryId': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'collegename': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'enquirydate': forms.DateInput(attrs={'class': 'form-control'}),
            'followup_date': forms.DateInput(attrs={'class': 'form-control'}),
            'choice': forms.Select(attrs={'class': 'form-control'}),
        }

class AdmissionCreateForm(ModelForm):
    class Meta:
        model = AdmissionNewModel
        fields = '__all__'
        widgets = {
            'admission_no': forms.TextInput(attrs={'class': 'form-control'}),
            'enquiryid': forms.Select(attrs={'class': 'form-control'}),
            'coursefees': forms.NumberInput(attrs={'class': 'form-control'}),
            'batchcode': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),

        }

class PaymentCreateForm(ModelForm):
    class Meta:
        model = PaymentNewModel
        fields = '__all__'
        widgets = {
            'admission_no': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control'}),
            'enquiryid': forms.Select(attrs={'class': 'form-control'}),
            # 'date': forms.DateInput(attrs={'class': 'form-control'}),

        }


class RegistrationForm(UserCreationForm):
  class Meta:
      model = User
      fields = ['username', 'password1', 'password2','first_name','last_name','email']
      widgets = {
          'username': forms.TextInput(attrs={'class': 'form-control'}),
          'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
          'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
          'first_name': forms.TextInput(attrs={'class': 'form-control'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control'}),
          'email': forms.EmailInput(attrs={'class': 'form-control'}),
          # 'date': forms.DateInput(attrs={'class': 'form-control'}),

      }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=130)


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_name': forms.PasswordInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),

            # 'date': forms.DateInput(attrs={'class': 'form-control'}),

        }

class StudentForm(ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'total_fees': forms.TextInput(attrs={'class': 'form-control'}),

            # 'date': forms.DateInput(attrs={'class': 'form-control'}),

        }



