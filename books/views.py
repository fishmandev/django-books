from django.shortcuts import render

# Create your views here.
def default_view(request, *args, **kwargs):
    return render(request, 'default.html', {})