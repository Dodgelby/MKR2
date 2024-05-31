from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from .models import Author
from django.contrib.auth.models import User
from django.test import Client
from .models import Book
from .views import book_detail, ordered_books, book_list
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

class AuthorDetailViewTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author', bio='This is a test bio.')

    def test_author_detail_view(self):
        response = self.client.get(reverse('author_detail', args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_detail.html')
        self.assertContains(response, self.author.name)
        self.assertContains(response, self.author.bio)

class AuthorListViewTestCase(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name='Author 1', bio='Bio 1')
        self.author2 = Author.objects.create(name='Author 2', bio='Bio 2')

    def test_author_list_view(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')
        self.assertContains(response, self.author1.name)
        self.assertContains(response, self.author2.name)
        self.assertContains(response, reverse('author_detail', args=[self.author1.id]))
        self.assertContains(response, reverse('author_detail', args=[self.author2.id]))


class BookViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.book = Book.objects.create(title="test",
                                        description="test", price=12, publication_date=datetime.now(), cover_image="test.png")
    def test_book_detail_view(self):
        url = reverse('book_detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_detail.html')

    def test_ordered_books_view(self):
        url = reverse('ordered_books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_book_list_view(self):
        url = reverse('book_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_list.html')

