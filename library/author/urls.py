from django.conf.urls import url

from . import views
from .views import AuthorList, AuthorCreateView, AuthorListView, AuthorDetailView

urlpatterns = [
    # url('', views.get_all_authors, name='authors_list'),
    # url('<int:id>/', views.get_by_id, name='get_author'),
    # url('delete/<int:id>/', views.delete_author_by_id, name='delete_author'),
    # url('clean/', views.delete_all_authors, name='delete_all_authors'),

    url(r'^authors/$', AuthorList.as_view()),

    url('rest_create/', AuthorCreateView.as_view()),
    url('rest_all/', AuthorListView.as_view()),
    url('rest_detail/<int:pk>/', AuthorDetailView.as_view()),

]

