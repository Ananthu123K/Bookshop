from django.db import models

# Create your models here.

class CategoryDb(models.Model):
    Category_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    Cover_Image=models.ImageField(upload_to='category_image',null=True,blank=True)

class BookDb(models.Model):
    Title=models.CharField(max_length=100,null=True,blank=True)
    Author=models.CharField(max_length=100,null=True,blank=True)
    Category=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Publisher=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    Cover_image=models.ImageField(upload_to="book_images",null=True,blank=True)