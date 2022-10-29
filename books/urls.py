from django.urls import path
from books import views

urlpatterns = [
    path('create/', views.book_create_view, name='book_create'),
    path('<int:id>/', views.book_detail_view, name='book_detail'),
    path('<int:id>/delete/', views.book_delete_view, name='book_delete'),
]
