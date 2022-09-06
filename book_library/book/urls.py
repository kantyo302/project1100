from django.urls import path
from . import views

urlpatterns = [ 
    path('book/',views.BookListViews.as_view(),name = 'book-list'),
    path('book/<int:pk>/detail/',views.BookDetailViews.as_view(),name = 'book-detail'),
    path('book/create/',views.BookCreateViews.as_view(),name = 'book-create'),
    path('book/<int:pk>/delete/',views.BookDeleteViews.as_view(),name = 'book-delete'),
    path('book/<int:pk>/update/',views.BookUpdateViews.as_view(),name = 'book-update')
]