from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from category.models import CategoryBlog
# Create your models here.
class Blogs(models.Model) :
     name = models.CharField(max_length=255)
     description = models.TextField()
     content = models.TextField()
     category = models.ForeignKey(CategoryBlog, on_delete= models.CASCADE)
     writer = models.CharField(max_length=255)
     views = models.IntegerField(default=0)
     image = models.ImageField(upload_to = "blogsImgFold", blank= True)
     create = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
          return self.name