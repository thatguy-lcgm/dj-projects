from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, )
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
    website_url = models.CharField(max_length=255, blank=True, null=True, )
    facebook_url = models.CharField(max_length=255, blank=True, null=True, )
    twitter_url = models.CharField(max_length=255, blank=True, null=True, )
    instagram_url = models.CharField(max_length=255, blank=True, null=True, )
    pinterest_url = models.CharField(max_length=255, blank=True, null=True, )


    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=225)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=225,)  # , default="My Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=225, default='others')
    snippet = models.CharField(max_length=225)
    likes = models.ManyToManyField(User, related_name='blog_post')


    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return f'{self.title} |  {self.author}'


    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.post.title} {self.name}'
