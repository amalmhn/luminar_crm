from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from .models import *
from django.views.generic import TemplateView
from .forms import RegistrationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
# Create your views here.

class CourseCreateView(TemplateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'luminarApp/courseCreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        course = self.model.objects.all()
        self.context['form'] = form
        self.context['course'] = course
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coursecreate')
        else:
            return render(request,self.template_name,self.context)

class CourseEditView(TemplateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'luminarApp/courseEdit.html'
    context = {}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        course = self.get_object(id)
        form = self.form_class(instance=course)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        course = self.get_object(id)
        form = self.form_class(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('coursecreate')
        else:
            return render(request,self.template_name,self.context)

class CourseDeleteView(TemplateView):
    model = Course
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        course = self.get_object(id)
        course.delete()
        return redirect('coursecreate')





class HomeView(TemplateView):
    template_name = 'luminarApp/home.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

    # @method_decorator(login_required,name='centerhead')
class CenterHeadView(TemplateView):
    model = EmployeeModel
    template_name = 'luminarApp/centerHead.html'
    context = {}
    def get(self, request, *args, **kwargs):
        employee = self.model.objects.all()
        self.context['employee'] = employee
        return render(request,self.template_name,self.context)

class BatchCreateView(TemplateView):
    model = Batch
    form_class = BatchCreateForm
    template_name = 'luminarApp/batchCreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        batch = self.model.objects.all()
        self.context['form'] = form
        self.context['batch'] = batch
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('batchcreate')
        else:
            return render(request,self.template_name,self.context)

class BatchEditView(TemplateView):
    model = Batch
    form_class = BatchCreateForm
    template_name = 'luminarApp/batchedit.html'
    context = {}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        batch = self.get_object(id)
        form = self.form_class(instance=batch)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        batch = self.get_object(id)
        form = self.form_class(request.POST,instance=batch)
        if form.is_valid():
            form.save()
            return redirect('batchcreate')
        else:
            return render(request, self.template_name, self.context)

class BatchDeleteView(TemplateView):
    model = Batch
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        batch = self.get_object(id)
        batch.delete()
        return redirect('batchcreate')

class EnquiryCreateView(TemplateView):
    model = EnquiryThree
    form_class = EnquiryCreateForm
    template_name = 'luminarApp/enquirycreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        enq = self.model.objects.all()
        enquiry = self.model.objects.last()
        if enquiry:
            last_enquiryid = enquiry.enquiryId
            lst = int(last_enquiryid)+1
            enquiryId = str(lst)
        else:
            enquiryId='1000'

        form = self.form_class(initial={'enquiryId':enquiryId})

        self.context['form'] = form
        self.context['enq'] = enq
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('enquirycreate')
        else:
            print('not saved')
            return render(request, self.template_name, self.context)

class EnquiryEditView(TemplateView):
    model = EnquiryThree
    form_class = EnquiryCreateForm
    template_name = 'luminarApp/enquiryedit.html'
    context = {}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        enquiry = self.get_object(id)
        form = self.form_class(instance=enquiry)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        enquiry = self.get_object(id)
        form = self.form_class(request.POST,instance=enquiry)
        if form.is_valid():
            form.save()
            return redirect('enquirycreate')
        else:
            return render(request, self.template_name, self.context)

class EnquiryDeleteView(TemplateView):
    model = EnquiryThree
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        enquiry = self.get_object(id)
        enquiry.delete()
        return redirect('enquirycreate')

class AdmissionCreateView(TemplateView):
    model = Admission
    form_class = AdmissionCreateForm
    template_name = 'luminarApp/admissioncreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        adm = self.model.objects.all()
        admission = self.model.objects.last()
        if admission:
            last_admission_no = admission.admission_no
            lst = int(last_admission_no) + 1
            admission_no = str(lst)
        else:
            admission_no = '2000'

        form = self.form_class(initial={'admission_no': admission_no})

        self.context['form'] = form
        self.context['adm'] = adm
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admissioncreate')
        else:
            return render(request, self.template_name, self.context)

class AdmissionEditView(TemplateView):
    model = Admission
    form_class = AdmissionCreateForm
    template_name = 'luminarApp/admissionedit.html'
    context = {}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        admission = self.get_object(id)
        form = self.form_class(instance=admission)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        admission = self.get_object(id)
        form = self.form_class(request.POST,instance=admission)
        if form.is_valid():
            form.save()
            return redirect('admissioncreate')
        else:
            return render(request, self.template_name, self.context)

class AdmissionDeleteView(TemplateView):
    model = Admission
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        admission = self.get_object(id)
        admission.delete()
        return redirect('admissioncreate')

class PaymentCreateView(TemplateView):
    model = Payment
    form_class = PaymentCreateForm
    template_name = 'luminarApp/paymentcreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        admission = self.model.objects.all()
        self.context['form'] = form
        self.context['admission'] = admission
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paymentcreate')
        else:
            return render(request,self.template_name,self.context)

class PaymentEditView(TemplateView):
    model = Payment
    form_class = PaymentCreateForm
    template_name = 'luminarApp/paymentedit.html'
    context = {}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        payment = self.get_object(id)
        form = self.form_class(instance=payment)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        payment = self.get_object(id)
        form = self.form_class(request.POST,instance=payment)
        if form.is_valid():
            form.save()
            return redirect('paymentcreate')
        else:
            return render(request, self.template_name, self.context)

class PaymentDeleteView(TemplateView):
    model = Payment
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        payment = self.get_object(id)
        payment.delete()
        return redirect('paymentcreate')

class CounselorView(TemplateView):
    model = StudentModel
    template_name = 'luminarApp/counselor.html'
    context = {}
    def get(self, request, *args, **kwargs):
        student = self.model.objects.all()
        self.context['student'] = student
        return render(request,self.template_name,self.context)


class RegistrationView(TemplateView):
    form_class = RegistrationForm
    form_class2 = LoginForm
    template_name = 'luminarApp/registration.html'
    model = User
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # self.context['form'] = self.form_class2
            # return render(request,'luminarApp/login.html',self.context)
            return redirect('signin')
        else:
            self.context['form'] = form
            return render(request, self.template_name, self.context)

class LoginView(TemplateView):
    template_name = 'luminarApp/login.html'
    form_class = LoginForm
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username=uname,password=pwd)
            if uname=='luminaruser':
                if user!=None:
                    login(request,user)
                    return redirect('centerhead')
                else:
                    form = self.form_class(request.POST)
                    self.context['form'] = form
                    return render(request, self.template_name, self.context)
            else:
                if user!=None:
                    login(request, user)
                    return redirect('counselor')

            # if user!=None:
            #     login(request,user)
            #     return redirect('home')

class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

class EmployeeView(TemplateView):
    model = EmployeeModel
    form_class = EmployeeForm
    template_name = 'luminarApp/employeecreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        employee = self.model.objects.all()
        self.context['form'] = form
        self.context['employee'] = employee
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeecreate')
        else:
            return render(request,self.template_name,self.context)

class EmployeeEditView(TemplateView):
    model = EmployeeModel
    form_class = EmployeeForm
    template_name = 'luminarApp/employeeedit.html'
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        employee = self.get_object(id)
        form = self.form_class(instance=employee)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        employee = self.get_object(id)
        form = self.form_class(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employeecreate')
        else:
            return render(request,self.template_name,self.context)

class EmployeeDeleteView(TemplateView):
    model = EmployeeModel
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        employee = self.get_object(id)
        employee.delete()
        return redirect('employeecreate')

class StudentView(TemplateView):
    model = StudentModel
    form_class = StudentForm
    template_name = 'luminarApp/studentcreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        student = self.model.objects.all()
        self.context['form'] = form
        self.context['student'] = student
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentcreate')
        else:
            return render(request,self.template_name,self.context)

class StudentEditView(TemplateView):
    model = StudentModel
    form_class = StudentForm
    template_name = 'luminarApp/studentedit.html'
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id=kwargs.get('pk')
        student = self.get_object(id)
        form = self.form_class(instance=student)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        student = self.get_object(id)
        form = self.form_class(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentcreate')
        else:
            return render(request,self.template_name,self.context)

class StudentDeleteView(TemplateView):
    model = StudentModel
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        student = self.get_object(id)
        student.delete()
        return redirect('studentcreate')


