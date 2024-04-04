from unittest import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
    """
    Test case for the Books API endpoints. /* fff //fff */
    """

    def setUp(self):
        self.book_1 = Book.objects.create(title='Book 1', price='152', author_name='Админ')
        self.book_2 = Book.objects.create(title='Book 2 Админ', price='399.23', author_name='Админ')

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_author_name(self):
        url = reverse('book-list')
        response = self.client.get(url, {'author_name': 'Админ'})
        serializer_data = BookSerializer([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_sort_by_price(self):
        """
        Test sorting books by price.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': '-price'})
        sorted_books = Book.objects.all().order_by('-price')
        serializer_data = BookSerializer(sorted_books, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print(sorted_books)
        print(response.data)
