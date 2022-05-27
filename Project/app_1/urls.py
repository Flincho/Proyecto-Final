from django.urls import path

from app_1 import views

urlpatterns = [
    path('', views.index, name='Home'),
    #path('profesors', views.profesors, name='Profesors'),
    #path('courses', views.courses, name='Courses'),
    #path('students', views.students, name='Students'),
    #path('homeworks', views.homeworks, name='Homeworks'),
    #path('formHTML', views.form_hmtl),
    #path('course-django-forms', views.course_forms_django, name='CourseDjangoForms'),
    #path('profesor-django-forms', views.profesor_forms_django, name='ProfesorDjangoForms'),
    #path('homework-django-forms', views.homework_forms_django, name='HomeworkDjangoForms'),
    #path('search', views.search, name='Search'),

    path('suppliers', views.SupplierListView.as_view(), name='supplier-list'),
    path('supplier/add/', views.SupplierCreateView.as_view(), name='supplier-add'),
    path('supplier/<int:pk>/detail', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('supplier/<int:pk>/update', views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete', views.SupplierDeleteView.as_view(), name='supplier-delete'),
]
