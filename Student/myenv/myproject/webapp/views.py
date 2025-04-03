from django.shortcuts import render ,redirect
from .forms import Studentform
from .models import Student

"""
def home(request):
    return render(request, 'webapp/index.html')
"""
# Home view - Redirects to the student list page
def home(request):
     #return redirect('student_list')  # Redirects '/' to '/students/'
     return render(request, 'webapp/home.html')

# View to handle the student form (Add Student)
def student_form(request):
    if request.method == 'POST':
        form = Studentform(request.POST)  # Instantiate form with POST data
        if form.is_valid():
            form.save()  # Save student to database
            return redirect('student_list')  # Redirect to student list page
    else:
        form = Studentform()  # Empty form for GET request

    return render(request, 'webapp/student_form.html', {'form': form})

# View to list all students
def student_list(request):
    students = Student.objects.all()  # Get all students
    student_count = students.count()  # Count total students

    return render(request, 'webapp/student_list.html', {
        'students': students,
        'student_count': student_count  # Pass count to template
    })