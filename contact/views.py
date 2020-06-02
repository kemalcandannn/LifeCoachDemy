from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.

def contact_index(request):
    if not request.user.is_superuser:
        return Http404()

    contact_list = Contact.objects.all()
    query = request.GET.get('q')
    if query:
        contact_list = contact_list.filter(
            Q(full_name__icontains=query) |
            Q(name__icontains=query) |
            Q(eMail__icontains=query) |
            Q(content__icontains=query) |
            Q(answered__icontains=query) |
            Q(post_answered_user__first_name__icontains=query) |
            Q(post_answered_user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(contact_list, 5)
    page = request.GET.get('sayfa')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'contact/index.html', {'contacts': contacts})

def contact_detail(request, slug):
    contact = get_object_or_404(Contact, slug=slug)
    context = {
        'contact' : contact
    }
    return render(request, 'contact/detail.html', context)

def contact_create(request):
    form = ContactForm(request.POST or None) # , request.FILES or None >>>> Formun içinde dosya göndermek için kullanılır

    if form.is_valid():
        contact = form.save(commit=False)
        contact.staff = request.user
        contact.save()

        messages.success(request, '"' + contact.name + '" başarıyla iletildi.')
        return HttpResponseRedirect(contact.get_absolute_url())

    context = {
        'form' : form
    }
    return render(request, 'contact/contactForm.html', context)

def contact_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    contact = get_object_or_404(Contact, slug=slug)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        messages.success(request, '"' + contact.name + '" başarıyla güncellendi.')
        return HttpResponseRedirect(contact.get_absolute_url())

    context = {
        'form' : form
    }

    return render(request, 'contact/contactForm.html', context)

def contact_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    contact = get_object_or_404(Contact, slug=slug)
    contact.delete()
    messages.error(request, '"' + contact.name + '" başarıyla silindi.')
    return redirect('contact:index')
