from unittest import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(title='Book 1', price='152.00')
        book_2 = Book.objects.create(title='Book 2', price='399.23')
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                "id": book_1.id,
                "title": book_1.title,
                "price": book_1.price,
            },
            {
                "id": book_2.id,
                "title": book_2.title,
                "price": book_2.price,
            }
        ]
        self.assertEqual(expected_data, data)

# coverage run --source='.' ./manage.py test .

# coverage report

#coverage html
