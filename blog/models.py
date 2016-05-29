
from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey(User, verbose_name="Autor")

    title = models.CharField(max_length=200, verbose_name="Título")

    text = models.TextField(verbose_name="Texto")

    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data de Criação")

    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de Publicação")


    def publish(self):

        self.published_date = timezone.now()

        self.save()


    def approved_comments(self):

        return self.comments.filter(approved_comment=True)


    def __str__(self):

        return self.title



class Comment(models.Model):

    post = models.ForeignKey(Post, related_name='comments')

    author = models.CharField(max_length=200)

    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    approved_comment = models.BooleanField(default=False)


    def approve(self):

        self.approved_comment = True

        self.save()


    def __str__(self):

        return self.text






