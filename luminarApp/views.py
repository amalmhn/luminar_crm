from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import TemplateView
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

class CenterHeadView(TemplateView):
    template_name = 'luminarApp/centerHead.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

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
        form = self.form_class
        enquiry = self.model.objects.all()
        self.context['form'] = form
        self.context['enquiry'] = enquiry
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
        form = self.form_class
        admission = self.model.objects.all()
        self.context['form'] = form
        self.context['admission'] = admission
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
    template_name = 'luminarApp/counselor.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)