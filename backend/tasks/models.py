from django.db import models
#from django.contrib.auth.models import User
from accounts.models import UserAccount
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'