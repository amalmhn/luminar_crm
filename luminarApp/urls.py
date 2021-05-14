"""luminarCr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from luminarApp import views
urlpatterns = [
    path('coursecreate',CourseCreateView.as_view(),name='coursecreate'),
    path('courseedit/<int:pk>',CourseEditView.as_view(),name='courseedit'),
    path('coursedelete/<int:pk>',CourseDeleteView.as_view(),name='coursedelete'),
    path('home',HomeView.as_view(),name='home'),
    path('centerhead',CenterHeadView.as_view(),name='centerhead'),
    path('batchcreate',BatchCreateView.as_view(),name='batchcreate'),
    path('batchedit/<int:pk>',BatchEditView.as_view(),name='batchedit'),
    path('batchdelete/<int:pk>',BatchDeleteView.as_view(),name='batchdelete'),
    path('enquirycreate',EnquiryCreateView.as_view(),name='enquirycreate'),
    path('enquiryedit/<int:pk>',EnquiryEditView.as_view(),name='enquiryedit'),
    path('enquirydelete/<int:pk>',EnquiryDeleteView.as_view(),name='enquirydelete'),
    path('admissioncreate',AdmissionCreateView.as_view(),name='admissioncreate'),
    path('admissionedit/<int:pk>',AdmissionEditView.as_view(),name='admissionedit'),
    path('admissiondelete/<int:pk>',AdmissionDeleteView.as_view(),name='admissiondelete'),
    path('paymentcreate',PaymentCreateView.as_view(),name='paymentcreate'),
    path('paymentedit/<int:pk>',PaymentEditView.as_view(),name='paymentedit'),
    path('paymentdelete/<int:pk>',PaymentDeleteView.as_view(),name='paymentdelete'),
    path('counselor',CounselorView.as_view(),name='counselor'),
    path('register',RegistrationView.as_view(),name='register'),
    path('signin',LoginView.as_view(),name='signin'),
    path('signout',LogoutView.as_view(),name='signout'),
    path('employeecreate',EmployeeView.as_view(),name='employeecreate'),
    path('employeeedit/<int:pk>',EmployeeEditView.as_view(),name='employeeedit'),
    path('employeedelete/<int:pk>',EmployeeDeleteView.as_view(),name='employeedelete'),
    path('studentcreate',StudentView.as_view(),name='studentcreate'),
    path('studentedit/<int:pk>',StudentEditView.as_view(),name='studentedit'),
    path('studentdelete/<int:pk>',StudentDeleteView.as_view(),name='studentdelete'),
]
