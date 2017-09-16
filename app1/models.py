from django.db import models


class Publication (models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Comment (models.Model):
    author_name = models.CharField(max_length=100)
    body = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.author_name, self.body)


class Article (models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
