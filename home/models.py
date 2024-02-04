from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    version = models.DecimalField(max_digits=4, decimal_places=1)
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_by", on_delete=models.SET("USER_NOT_FOUND")
    )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, related_name="updated_by", on_delete=models.SET("USER_NOT_FOUND")
    )
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.version}"

    def save(self, *args, **kwargs):
        
        super(Document, self).save(*args, **kwargs)

        DocumentHistory.objects.create(
            document=self,
            name=self.name,
            version=self.version,
            content=self.content,
            created_at=self.created_at,
            created_by=self.created_by,
            updated_at=self.updated_at,
            updated_by=self.updated_by,
            active=self.active,
        )


class DocumentHistory(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    version = models.DecimalField(max_digits=4, decimal_places=1)
    content = RichTextField()

    created_at = models.DateTimeField()
    created_by = models.ForeignKey(
        User, related_name="h_created_by", on_delete=models.SET("USER_NOT_FOUND")
    )
    updated_at = models.DateTimeField()
    updated_by = models.ForeignKey(
        User, related_name="h_updated_by", on_delete=models.SET("USER_NOT_FOUND")
    )
    active = models.BooleanField(default=True)

    document = models.ForeignKey(
        Document, related_name="history", on_delete=models.SET("DOCUMENT_NOT_FOUND")
    )

    class Meta:
        ordering = ["-pk"]

    def __str__(self) -> str:
        return f"{self.name} - {self.version}"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="commented_by", on_delete=models.SET("USER_NOT_FOUND")
    )
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)



