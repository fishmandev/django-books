from django.urls import path
from books import views

urlpatterns = [
    path('create/', views.book_create_view, name='book_create'),
    path('', views.book_list_view, name='book_list'),
    path('<slug:slug>/', views.book_detail_view, name='book_detail'),
    path('<int:id>/delete/', views.book_delete_view, name='book_delete'),
]
