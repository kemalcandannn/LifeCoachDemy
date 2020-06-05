from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from course.models import Course
from project.models import Project
from user.models import User


def home_view(request):

    course_list = Course.objects.raw('SELECT * FROM course_course')
    query = request.GET.get('q')

    if query:
        course_list = Course.objects.raw('SELECT DISTINCT * FROM course_course WHERE '
                 '(lower(name) like \'%' + str(query).lower() + '%\') or '
                 '(lower(subject) like \'%' + str(query).lower() + '%\') or '
                 '(lower(content) like \'%' + str(query).lower() + '%\')')


    page = request.GET.get('sayfa1')

    paginator = Paginator(course_list, 5) #Show 5 courses per page

    try:
        course_list = paginator.page(page)
    except PageNotAnInteger:
        # Show 5 courses per page
        course_list = paginator.page(1)
    except EmptyPage:
        # Show 5 courses per page
        course_list = paginator.page(paginator.num_pages)


    project_list = Project.objects.raw('SELECT * FROM project_project')
    page = request.GET.get('sayfa2')

    query2 = request.GET.get('q2')

    if query2:
        project_list = Project.objects.raw('SELECT DISTINCT * FROM project_project WHERE '
                 '(lower(name) like \'%' + str(query2).lower() + '%\') or '
                 '(lower(content) like \'%' + str(query2).lower() + '%\') or '
                 '(lower(deadline) like \'%' + str(query2).lower() + '%\')')

    paginator = Paginator(project_list, 5) #Show 5 courses per page

    try:
        project_list = paginator.page(page)
    except PageNotAnInteger:
        project_list = paginator.page(1)
    except EmptyPage:
        project_list = paginator.page(paginator.num_pages)

    user_list = User.objects.raw('SELECT * FROM user_user')
    query3 = request.GET.get('q3')

    if query3:
        user_list = User.objects.raw('SELECT DISTINCT * FROM user_user WHERE '
                 '(lower(name) like \'%' + str(query3).lower() + '%\') or '
                 '(lower(surname) like \'%' + str(query3).lower() + '%\') or '
                 '(lower(mail) like \'%' + str(query3).lower() + '%\') or '
                 '(lower(cep_tel) like \'%' + str(query3).lower() + '%\') or '
                 '(lower(experience) like \'%' + str(query3).lower() + '%\') or '
                 '(lower(register_date) like \'%' + str(query3).lower() + '%\')')

    page = request.GET.get('sayfa3')

    paginator = Paginator(user_list, 5) #Show 5 courses per page

    try:
        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)


    context = {
        'courses':  course_list,
        'projects': project_list,
        'users': user_list,
    }

    return render(request, 'home.html', context)
