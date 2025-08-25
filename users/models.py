from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here
class Profile(models.Model):
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username