from django.shortcuts import render
from django.db.models import Q

from app_1.models import *
# from app_1.forms import *



def index(request):
    return render(request, "app_1/home.html")

#
#ef profesors(request):
#    profesors = Profesor.objects.all()
#
#    context_dict = {
#        'profesors': profesors
#    }
#
#    return render(
#        request=request,
#        context=context_dict,
#       template_name="app_1/profesors.html"
#    )
#
#
#ef courses(request):
#    courses = Course.objects.all()
#
#    context_dict = {
#        'courses': courses
#    }
#
#    return render(
#        request=request,
#        context=context_dict,
#       template_name="app_1/courses.html"
#    )
#
#
#ef students(request):
#    students = Student.objects.all()
#
#    context_dict = {
#        'students': students
#    }
#
#    return render(
#        request=request,
#        context=context_dict,
#       template_name="app_1/students.html"
#    )
#
#
#ef homeworks(request):
#    homeworks = Homework.objects.all()
#
#    context_dict = {
#        'homeworks': homeworks
#    }
#
#    return render(
#        request=request,
#        context=context_dict,
#       template_name="app_1/homeworks.html"
#    )
#

#def form_hmtl(request):
#
#    if request.method == 'POST':
#        course = Course(name=request.POST['name'], code=request.POST['code'])
#        course.save()
#
#        courses = Course.objects.all()
#        context_dict = {
#            'courses': courses
#        }
#
#        return render(
#            request=request,
#            context=context_dict,
#            template_name="app_1/courses.html"
#        )
#
#    return render(
#        request=request,
#        template_name='app_1/formHTML.html'
#    )
#
#
#def course_forms_django(request):
#    if request.method == 'POST':
#        course_form = CourseForm(request.POST)
#        if course_form.is_valid():
#            data = course_form.cleaned_data
#            course = Course(name=data['name'], code=data['code'])
#            course.save()
#
#            courses = Course.objects.all()
#            context_dict = {
#                'courses': courses
#            }
#            return render(
#                request=request,
#                context=context_dict,
#                template_name="app_1/courses.html"
#            )
#
#    course_form = CourseForm(request.POST)
#    context_dict = {
#        'course_form': course_form
#    }
#    return render(
#        request=request,
#        context=context_dict,
#        template_name='app_1/course_django_forms.html'
#    )
#
#
#def profesor_forms_django(request):
#    if request.method == 'POST':
#        profesor_form = ProfesorForm(request.POST)
#        if profesor_form.is_valid():
#            data = profesor_form.cleaned_data
#            profesor = Profesor(
#                name=data['name'],
#                last_name=data['last_name'],
#                email=data['email'],
#                profession=data['profession'],
#            )
#            profesor.save()
#
#            profesors = Profesor.objects.all()
#            context_dict = {
#                'profesors': profesors
#            }
#            return render(
#                request=request,
#                context=context_dict,
#                template_name="app_1/profesors.html"
#            )
#
#    profesor_form = ProfesorForm(request.POST)
#    context_dict = {
#        'profesor_form': profesor_form
#    }
#    return render(
#        request=request,
#        context=context_dict,
#        template_name='app_1/profesor_django_forms.html'
#    )
#
#
#def homework_forms_django(request):
#    if request.method == 'POST':
#        homework_form = HomeworkForm(request.POST)
#        if homework_form.is_valid():
#            data = homework_form.cleaned_data
#            homework = Homework(
#                name=data['name'],
#                due_date=data['due_date'],
#                is_delivered=data['is_delivered'],
#            )
#            homework.save()
#
#            homeworks = Homework.objects.all()
#            context_dict = {
#                'homeworks': homeworks
#            }
#            return render(
#                request=request,
#                context=context_dict,
#                template_name="app_1/homeworks.html"
#            )
#
#    homework_form = HomeworkForm(request.POST)
#    context_dict = {
#        'homework_form': homework_form
#    }
#    return render(
#        request=request,
#        context=context_dict,
#        template_name='app_1/homework_django_forms.html'
#    )
#

def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        courses = Course.objects.filter(name__contains=search_param)
        context_dict = {
            'courses': courses
        }
    elif request.GET['code_search']:
        search_param = request.GET['code_search']
        courses = Course.objects.filter(code__contains=search_param)
        context_dict = {
            'courses': courses
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        courses = Course.objects.filter(query)
        context_dict = {
            'courses': courses
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_1/home.html",
    )


from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class SupplierListView(ListView):
    model = Supplier
    template_name = "app_1/supplier_list.html"


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "app_1/supplier_detail.html"


class SupplierCreateView(CreateView):
    model = Supplier
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_1:supplier-list')
    fields = ['name', 'phone', 'email', 'bank_account', 'working_since']


class SupplierUpdateView(UpdateView):
    model = Supplier
    # template_name = "app_coder/supplier_form.html"
    # success_url = "/app_coder/supplier"
    success_url = reverse_lazy('app_1:supplier-list')
    fields = ['name', 'phone', 'email', 'bank_account']
