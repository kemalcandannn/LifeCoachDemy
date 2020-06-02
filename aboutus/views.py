from django.shortcuts import render

def aboutUs_view(request):

    context = {}
    return render(request, 'aboutUs.html', context)
