from django.urls import path
from .views import student_list, student_form ,home

"""urlpatterns = [
    path('',views.home , name="home")                 #home -> function name in views.py
]"""

urlpatterns = [
    path('', home , name='home'),   # this handles /
    path('add-student/', student_form,name='add_student'),
    path('students/',student_list,name='student_list'),
]