from django.contrib.auth import models as auth_model
from django.db import models


class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(auth_model.User, on_delete=models.CASCADE)


