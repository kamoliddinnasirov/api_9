from django.db import models
from django.contrib.auth.models import User

"""

"""

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Foydalanuvchi', on_delete=models.CASCADE)


    def __str__(self):
        return self.title 
    

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name