from django.shortcuts import render
from .models import Student
from .forms import StudentForm

def student_list(request):
    # Handle form submission (POST request)
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()

    # Initialize the query to get all students
    students = Student.objects.all()

    # Handle search (by name or student ID)
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(name__icontains=search_query) | students.filter(sid__icontains=search_query)

    # Handle branch filter
    branch_filter = request.GET.get('branch', '')
    if branch_filter:
        students = students.filter(branch=branch_filter)

    # Pass the form and the filtered students list to the template
    context = {
        'form': form,
        'students': students,
        'search_query': search_query,
        'branch_filter': branch_filter
    }

    return render(request, 'student_list.html', context)
