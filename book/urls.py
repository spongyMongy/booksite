from django.urls import include, path
from rest_framework import routers
from book.views import  BooksAPIView
from book.views import  BooksAPISearchView

from book.views import  OpinionsAPI_APIView
from book.views import  BooksAPI_APIView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    ###path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',  BooksAPIView.as_view(),  name='books_list'),
    path('home/', BooksAPIView.as_view(), name='books_list_home'),
    path('books/', BooksAPISearchView.as_view(),  name='book_results'),
    path('opinionsapi/', OpinionsAPI_APIView.as_view()),
    path('booksapi/', BooksAPI_APIView.as_view()),

]