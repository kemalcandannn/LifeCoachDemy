from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.

def project_index(request):
    project_list = list(Project.objects.raw('SELECT * FROM project_project WHERE project_owner_id = ' + str(request.user.id) ))
    query = request.GET.get('q')

    if query:
        project_list = list(Project.objects.raw('SELECT DISTINCT * FROM project_project WHERE '
                 '(lower(name) like \'%' + str(query).lower() + '%\') or '
                 '(lower(content) like \'%' + str(query).lower() + '%\') or '
                 '(lower(deadline) like \'%' + str(query).lower() + '%\')'))

    paginator = Paginator(project_list, 5) #Show 5 courses per page

    page = request.GET.get('sayfa')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # Show 5 courses per page
        projects = paginator.page(1)
    except EmptyPage:
        # Show 5 courses per page
        projects = paginator.page(paginator.num_pages)

    return render(request, 'project/index.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project' : project
    }
    return render(request, 'project/detail.html', context)

def project_create(request):
    if not request.user.is_authenticated:
        return Http404()

    form = ProjectForm(request.POST or None, request.FILES or None) # , request.FILES or None >>>> Formun içinde dosya göndermek için kullanılır

    if form.is_valid():
        project = form.save(commit=False)
        project.project_owner = request.user
        project.save()

        messages.success(request, '"' + project.name + '" Projesi başarılı bir şekilde oluşturuldu.')
        return HttpResponseRedirect(project.get_absolute_url())

    context = {
        'form' : form
    }
    return render(request, 'project/form.html', context)

def project_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    project = get_object_or_404(Project, slug=slug)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if form.is_valid():
        form.save()
        messages.success(request, '"' + project.name + '" Projesi başarılı bir şekilde güncellendi.')
        return HttpResponseRedirect(project.get_absolute_url())

    context = {
        'form' : form
    }

    return render(request, 'project/form.html', context)

def project_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    project = get_object_or_404(Project, slug=slug)
    project.delete()
    messages.error(request, '"' + project.name + '" Projesi başarılı bir şekilde silindi.')
    return redirect('project:index')
