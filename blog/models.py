from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from tinymce import models as tinymce_models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    
    def __str__(self) -> str:
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=500,null=True)
    summary = models.CharField(max_length=100, null=True)
    post = tinymce_models.HTMLField()
    image = models.ImageField(default='writing.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=500)
    category = models.ManyToManyField(Category,default='test', blank=True)
    date = models.DateTimeField(default=timezone.now)

    # Get comments with no parent, that is top level comments
    # def get_comments(self):
    #     return self.comments.filter(parent=None)
  
    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    commentpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent =  models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='+')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.body


    #   get child comments
    @property
    def children(self):
        return Comment.objects.filter(parent=self).all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False