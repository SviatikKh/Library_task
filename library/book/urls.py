from django.conf.urls import url

from . import views
from .views import BookList, BookCreateView, BookListView, BookDetailView

urlpatterns = [
    # url('', views.get_all, name='book_get_all'),
    # url('<int:id>/', views.get_by_id, name='book_get_by_id'),
    # url('delete/<int:id>/', views.delete_by_id, name='book_delete_by_id'),
    # url('clear-author/<int:id>/', views.clear_authors, name='book_clear_author'),

    url(r'^books/$', BookList.as_view()),

    url('rest_create_book/', BookCreateView.as_view()),
    url('rest_all_book/', BookListView.as_view()),
    url('rest_detail_book/<int:pk>/', BookDetailView.as_view()),

]

