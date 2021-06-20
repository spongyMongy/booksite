from .serializers import BooksSerializer
from .models import Books
from .serializers import OpinionsSerializer
from .models import Opinions

from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from django.shortcuts import redirect
from django.contrib import messages



## Using DRF, creating Books list view
class BooksAPIView(generics.ListCreateAPIView):
    search_fields = ['title', 'ISBN', 'author', 'type']
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Booklist.html'

    def get(self, request):
        queryset = Books.objects.all()
        return Response({'books': queryset})




## Using DRF, creating Books search results view
class BooksAPISearchView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Bookresults.html'

    def get(self, request):
        query = self.request.GET.get('searchit')
        if query is not None and query!='':
            queryset = Books.objects.filter(title__icontains=query)  # new

            ## for having a valid list of books that have comments
            if(len(queryset)!=0 and queryset is not None):
                querySets = []
                booknameSets = []
                for x in range(len(queryset)):
                    try:
                        querysetOpinion = Opinions.objects.filter(ISBN_id__ISBN__icontains= queryset[x].ISBN      )
                        bookname=queryset[x]
                    except:
                        print('error with the query ' ,  queryset[0].title  )
                        response = redirect('/home')
                        return response

                    querySets.append(querysetOpinion)
                    booknameSets.append(bookname)
                bookset_wout_opinions=set()

                for x in booknameSets:
                    bookset_wout_opinions.add(x.title)

                ## for having a valid set of books that don't have comments
                for x in querySets:
                    for opinion in x:
                        for bookset in booknameSets:

                            if  opinion.from_book == bookset.title :
                                try:
                                    bookset_wout_opinions.remove(bookset.title)
                                except:
                                    continue

                booklist_wout_opinions=list(bookset_wout_opinions)
                no_reviews = 'No reviews yet for this title'
                return Response({'querySets': querySets   , 'booklist_wout_opinions' :booklist_wout_opinions , 'no_reviews': no_reviews })
            else:
                print('query result does not exist in database')
                messages.add_message(request, messages.INFO, ".: No result for the book you searched:-( Please check  some of our other great books   :.")
                response = redirect('/home')
                return response

        else:
            print('query is none')
            response = redirect('/home')
            return response




## Using DRF, creating Opinions  pure API view
class OpinionsAPI_APIView(generics.ListCreateAPIView):
    search_fields = ['rating','description', 'ISBN__ISBN']
    filter_backends = (filters.SearchFilter,)
    queryset =  Opinions.objects.all()
    serializer_class =  OpinionsSerializer


## Using DRF, creating Books  pure API view. You can use 'Filters' box in API view for additional search.
class BooksAPI_APIView(generics.ListCreateAPIView):
    search_fields = ['title', 'ISBN', 'author', 'type']
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
