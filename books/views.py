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
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("default")
    return render(request, 'create.html', {'form': form})

@login_required
def book_detail_view(request, id):
    obj = get_object_or_404(Book, id=id)
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