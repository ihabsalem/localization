from django.db import models
from language.models import Language
# Create your models here.


class Source(models.Model):
    name = models.CharField(primary_key = True, max_length=255, null=False)

    def __str__(self):
        return "{}".format(self.name)
