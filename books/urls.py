from django.urls import path
from .views import BookListView,BookDetailView,SearchResultsListView,Book_category,like,reservarlibro,libros_reservados
urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name="book_detail"),
    path("search/", SearchResultsListView.as_view(),name="search_results"),
    path('category/<slug>/',Book_category.as_view(),name='book_category'),
    path('like/<uuid:pk>/',like,name='like'),
    path('reserva/<uuid:pk>/',reservarlibro,name='reserva'),
    path('libros_reservados/',libros_reservados.as_view(),name='libros_reservados'),
]