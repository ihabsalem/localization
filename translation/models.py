from django.db import models
from language.models import Language
from source.models import Source
# Create your models here.


class Translation(models.Model):
    source = models.ForeignKey(Source, blank=False,on_delete=models.deletion.CASCADE, max_length=255, null=False)
    language = models.ForeignKey(Language, blank=False,on_delete=models.deletion.CASCADE, max_length=255, null=False)
    key = models.CharField(max_length=255, null=False)
    label = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.language, self.source, self.key,self.label)
