from django.db import models
from django.contrib.auth.models import User


# create my model here
class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return self.name.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated_on = models.DateTimeField(auto_now=True,auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
