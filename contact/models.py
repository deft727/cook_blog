from django.db import models
from ckeditor.fields import RichTextField


class ContactModel(models.Model):
    """класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True,null=True)
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'
    

class ContactLink(models.Model):
    ''' Класс модели контактов'''
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class About(models.Model):
    ''' класс модели страницы о нас '''
    name = models.CharField(max_length=50,default='')
    text = RichTextField()
    mini_text = RichTextField()
     
    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url
    
    def get_images(self):
        return self.about_images.order_by('-id')[1:]

    def __str__(self):
        return self.mini_text


class ImageAbout(models.Model):
    '''Класс модели изображений  о нас '''
    image = models.ImageField(upload_to="about/")
    page = models.ForeignKey(About,on_delete=models.CASCADE,related_name='about_images')
    alt = models.CharField(max_length=200)


class Social(models.Model):
    ''' класс модели соц сетей'''
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self) -> str:
        return self.name
