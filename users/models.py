from django.db import models
from django.contrib.auth.models import User
from blog.models import BlogPost,Category 
from tinymce import models as tinymce_models

from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = tinymce_models.HTMLField(null=True, blank=True, default='Say something About Yourself')
    image = models.ImageField(default='wes-hicks-4-EeTnaC1S4-unsplash.jpg',upload_to='profile_pics')
    interests = models.ManyToManyField(Category,blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # resize profile pic automically 
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            print('successful')