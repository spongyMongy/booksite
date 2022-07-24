from django.urls import include, path
from rest_framework import routers
from book.views import  BooksApiView
from book.views import  BooksApiSearchView

from book.views import  OpinionsApiApiView
from book.views import  BooksApiApiView

router = routers.DefaultRouter()


urlpatterns = [
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('', BooksApiView.as_view(), name='books_list'),
    path('home/', BooksApiView.as_view(), name='books_list_home'),
    path('books/', BooksApiSearchView.as_view(), name='book_results'),
    path('opinionsapi/', OpinionsApiApiView.as_view()),
    path('booksapi/', BooksApiApiView.as_view()),

]