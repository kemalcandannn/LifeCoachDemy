from django.shortcuts import render

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim' : request.user.get_full_name()
        }
    else:
        context = {
            'isim' : 'Misafir'
        }

    return render(request, 'home.html', context)
