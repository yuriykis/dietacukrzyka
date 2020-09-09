from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField("First Name", default="Yuriy", max_length=30)
    last_name = models.CharField("Last Name", default="Kis", max_length=30)

    def __str__(self):
        return self.first_name + self.last_name