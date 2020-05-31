from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Course
from .forms import CourseForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def course_index(request):
    course_list = Course.objects.all()
    query = request.GET.get('q')
    if query:
        course_list = course_list.filter(
            Q(staff__first_name__icontains=query) |
            Q(staff__last_name__icontains=query) |
            Q(name__icontains=query) |
            Q(content__icontains=query)
            ).distinct()

    paginator = Paginator(course_list, 5) #Show 5 courses per page

    page = request.GET.get('sayfa')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        # Show 5 courses per page
        courses = paginator.page(1)
    except EmptyPage:
        # Show 5 courses per page
        courses = paginator.page(paginator.num_pages)

    return render(request, 'course/index.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        'course' : course
    }
    return render(request, 'course/detail.html', context)

def course_create(request):
    if not request.user.is_authenticated:
        return Http404()

    form = CourseForm(request.POST or None) # , request.FILES or None >>>> Formun içinde dosya göndermek için kullanılır

    if form.is_valid():
        course = form.save(commit=False)
        course.staff = request.user
        course.save()

        messages.success(request, 'Başarılı bir şekilde oluşturuldu.')
        return HttpResponseRedirect(course.get_absolute_url())

    context = {
        'form' : form
    }
    return render(request, 'course/form.html', context)

def course_update(request, id):
    if not request.user.is_authenticated:
        return Http404()

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
    if not request.user.is_authenticated:
        return Http404()

    course = get_object_or_404(Course, id=id)
    course.delete()
    messages.error(request, 'Başarılı bir şekilde silindi.')
    return redirect('course:index')
