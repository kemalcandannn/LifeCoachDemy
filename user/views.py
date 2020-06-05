from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import User
from .forms import UserForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def user_index(request):
    user_list = User.objects.all()
    query = request.GET.get('q')
    if query:
        user_list = user_list.filter(
            Q(name__icontains=query)
            ).distinct()

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
    user.delete()
    messages.error(request, 'Kullanıcı başarılı bir şekilde silindi.')
    return redirect('user:index')

def profile_view(request):
    if not request.user.is_authenticated:
        return Http404()

    user = request.user

    context = {
        'user' : user
    }
    return render(request, 'user/profile_view.html', context)
