from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Course
from .forms import CourseForm
from django.contrib import messages
# Create your views here.

def course_index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        'course' : course
    }
    return render(request, 'course/detail.html', context)

def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        course = form.save()
        messages.success(request, 'Başarılı bir şekilde oluşturuldu.')
        return HttpResponseRedirect(course.get_absolute_url())

    context = {
        'form' : form
    }
    return render(request, 'course/form.html', context)

def course_update(request, id):
    course = get_object_or_404(Course, id=id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellendi.')
        return HttpResponseRedirect(course.get_absolute_url())

    context = {
        'form' : form
    }

    return render(request, 'course/form.html', context)

def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    messages.error(request, 'Başarılı bir şekilde silindi.')
    return redirect('course:index')
