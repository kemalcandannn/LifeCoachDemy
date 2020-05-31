from django.shortcuts import render

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim' : 'Kemal'
        }
    else:
        context = {
            'isim' : 'Misafir'
        }

    return render(request, 'home.html', context)
