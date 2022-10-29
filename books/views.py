from wsgiref.util import request_uri
from django.shortcuts import render, get_object_or_404
from .forms import BookForm
from .models import Book

# Create your views here.
def default_view(request, *args, **kwargs):
    queryset = Book.objects.all()
    return render(request, 'default.html', { "books": queryset })

def book_create_view(request, *args, **kwargs):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'create.html', {'form': form})

def book_detail_view(request, id):
    obj = get_object_or_404(Book, id=id)
    context = {
        'object': obj
    }
    return render(request, "detail.html", context)