from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BookSerializer


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price']
    search_fields = ['title', 'author_name']  # http://127.0.0.1:8000/book/?search=title
    ordering_fields = ['title', 'author_name', 'price']  # http://127.0.0.1:8000/book/?ordering=author_name
    # http://127.0.0.1:8000/book/?ordering=-price  По Убыванию
