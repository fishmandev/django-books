from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book

# Create your views here.
def default_view(request):
    queryset = Book.objects.all()
    return render(request, 'default.html', { "books": queryset })

@login_required
def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect("default")
    form = BookForm
    return render(request, 'create.html', {'form': form})

@login_required
def book_detail_view(request, slug):
    obj = get_object_or_404(Book, slug=slug)
    context = {
        'object': obj
    }
    return render(request, "detail.html", context)

@login_required
def book_delete_view(request, id):
    obj = get_object_or_404(Book, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("default")
    context = {
        "object": obj
    }
    return render(request, "delete.html", context)