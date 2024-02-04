from django.db import models
from ckeditor.fields import RichTextField


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    version = models.DecimalField(max_digits=4, decimal_places=2)
    content = RichTextField()


    class Meta:
        unique_together = ("name", "version")

