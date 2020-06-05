from django.contrib.auth import logout
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import User
from .forms import UserForm
from django.contrib import messages, auth
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def user_index(request):
    user_list = list(User.objects.raw('SELECT * FROM user_user WHERE user_id = ' + str(request.user.id) ))

    query = request.GET.get('q')
    if query:
        user_list = list(User.objects.raw('SELECT DISTINCT * FROM user_user WHERE '
                 '(lower(name) like \'%' + str(query).lower() + '%\') or '
                 '(lower(surname) like \'%' + str(query).lower() + '%\') or '
                 '(lower(mail) like \'%' + str(query).lower() + '%\') or '
                 '(lower(cep_tel) like \'%' + str(query).lower() + '%\') or '
                 '(lower(experience) like \'%' + str(query).lower() + '%\') or '
                 '(lower(register_date) like \'%' + str(query).lower() + '%\')'))

    paginator = Paginator(user_list, 5)

    page = request.GET.get('sayfa')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'user/index.html', {'users': users})

def user_detail(request, slug):
    user = get_object_or_404(User, slug=slug)
    context = {
        'user' : user
    }
    return render(request, 'user/detail.html', context)

def user_create(request):
    if not request.user.is_authenticated:
        return Http404()

    form = UserForm(request.POST or None, request.FILES or None) # , request.FILES or None >>>> Formun içinde dosya göndermek için kullanılır

    if form.is_valid():
        user = form.save(commit=False)
        user.user = request.user
        user.save()

        messages.success(request, 'Kullanıcı başarılı bir şekilde oluşturuldu.')
        return redirect('/home')


    context = {
        'form' : form
    }
    return render(request, 'user/form.html', context)

def user_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    user = get_object_or_404(User, slug=slug)
    form = UserForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Kullanıcı başarılı bir şekilde güncellendi.')
        return HttpResponseRedirect(user.get_absolute_url())

    context = {
        'form' : form
    }

    return render(request, 'user/form.html', context)

def user_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    user = get_object_or_404(User, slug=slug)
    request.user.delete()
    user.delete()
    logout(request)

    messages.error(request, 'Hesabınız başarılı bir şekilde silindi.')
    return redirect('/home')

def profile_view(request):
    if not request.user.is_authenticated:
        return Http404()


    user = list(User.objects.raw('SELECT DISTINCT * FROM user_user WHERE user_id = ' + str(request.user.id)))


    if not user:
        return redirect('user:create')

    context = {
        'user': user[0]
    }
    return render(request, 'user/profile_view.html', context)