from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class Tasks(models.Model):
    date_created= models.DateTimeField(auto_now_add=True)
    body= RichTextField(blank = False)
    
    def get_absolute_url(self):
        
        return reverse('home')
