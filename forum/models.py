from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()


class Comments(models.Model):
    comments_text = models.TextField(verbose_name="Текс коментария")
    comments_article = models.ForeignKey(Article,on_delete='', null=True, related_name='+')
    comments_from = models.ForeignKey(User,on_delete='')
    comments_date = models.DateTimeField(auto_now=True)


class News_up(models.Model):
    new_text = models.TextField()
    image = models.ImageField(upload_to='image')


    def __str__(self):
        return self.image.url

class Bany_photo(models.Model):
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.image.url


class Raz_photo(models.Model):
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.image.url


class Sport_zal_photo(models.Model):
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.image.url


class Rooms_photo(models.Model):
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.image.url