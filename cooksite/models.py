from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

    class MPTTMeta:
        order_insertion_by=['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


class Post(models.Model):
    author = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles')
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
        )
    tags = models.ManyToManyField(Tag,related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves  = models.CharField(max_length=100)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    direction = models.TextField()
    post = models.ForeignKey(
        Post,related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=150)
    message = models.TextField(max_length=500,help_text='Максимум 500 символов')
    post = models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE,)