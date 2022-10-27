from django.shortcuts import render
from .forms import BookForm

# Create your views here.
def default_view(request, *args, **kwargs):
    return render(request, 'default.html', {})

def book_create_view(request, *args, **kwargs):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'create.html', {'form': form})