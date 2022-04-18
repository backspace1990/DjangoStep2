from django.shortcuts import render

# Create your views here.
def homeapp_view(request):
    context = {
        'user': 'UMIT',

    }
    return render(request, 'home/homeapp.html', context)