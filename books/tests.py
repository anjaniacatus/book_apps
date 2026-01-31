from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from .models import Book, Review


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="testPass1234",
        )
        cls.special_permission = Permission.objects.get(codename="special_status")

        cls.book = Book.objects.create(
            title="La force des discrets",
            author="Susan Cain",
            price="25.00",
        )

        cls.review = Review.objects.create(
            book=cls.book, author=cls.user, review="An excellent review"
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "La force des discrets")
        self.assertEqual(f"{self.book.author}", "Susan Cain")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_book_detail_view_with_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("book_list"), follow=True)
        self.assertContains(response, "Sign In")

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email="reviewuser@email.com", password="testPass1234")
        response = self.client.get(reverse("book_list"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "La force des discrets")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view_with_permissions(self):
        self.client.login(email="reviewuser@email.com", password="testPass1234")
        self.user.user_permissions.add(self.special_permission)
        detail_url = self.book.get_absolute_url()
        response = self.client.get(detail_url, follow=True)
        self.assertEqual(response.status_code, 200)

        no_response = self.client.get("/books/12345", follow=True)
        self.assertEqual(no_response.status_code, 404)

        self.assertContains(response, "La force des discrets")
        self.assertContains(response, "An excellent review")
        self.assertTemplateUsed(response, "books/book_detail.html")
