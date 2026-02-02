import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]

        permissions = [("special_status", "Can read all books")]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review


class Image(models.Model):
    key = models.CharField(help_text="The public id of uploaded file", max_length=100)
    url = models.CharField(max_length=100)
    name = models.CharField(
        max_length=100, help_text="The original name of the uploaded image"
    )
    width = models.IntegerField(help_text="width in pixel")
    height = models.IntegerField(help_text="height in pixels")
    format = models.CharField(max_length=10)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
