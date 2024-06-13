from django.db import models

class XMLSchema(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='xml_schemas/')
    # Добавьте другие поля, если необходимо

    def __str__(self):
        return self.name