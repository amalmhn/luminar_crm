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