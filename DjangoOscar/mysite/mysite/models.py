from django.db import models
import datetime
from django.contrib.auth.models import User



class AI_Models(models.Model):
    
    name = models.CharField("Название", max_length=1000, null=True, blank=True)
    short_name = models.CharField("Короткое название", max_length=100, null=True, blank=True)
    mission = models.CharField("Назначение", max_length=1000, null=True, blank=True)
    link_github = models.CharField("Ссылка на github", max_length=1000, null=True, blank=True)
    ai_model = models.FileField("Ссылка для загрузки", upload_to='ai_model/', null=True, blank=True)
    version = models.CharField("Версия XML", max_length=20, null=True, blank=True)
    date_public = models.DateField("Дата публикации", default=datetime.date.today)
    date_upload = models.DateField("Дата загрузки на сайт", default=datetime.date.today)
    date_unused = models.DateField("Дата прекращения использования", default=datetime.date.today)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нейросеть для преобразования"  
        verbose_name_plural = "Нейросети для преобразования"

    # Добавьте другие поля, если необходимо

    def __str__(self):
        return self.name


class XMLSchema(models.Model):
    STAGE_CHOICES = (
        ('building', 'Этап проектирования'),
        ('exploitation', 'Этап строительства'),
    )

    name = models.CharField("Название", max_length=1000, null=True, blank=True)
    short_name = models.CharField("Короткое название", max_length=100, null=True, blank=True)
    stage = models.CharField("Этап", max_length=20, choices=STAGE_CHOICES, null=True)
    file_schem_xsl = models.FileField("Файл XML схемы (XSL)", upload_to='xml_schemas/', null=True, blank=True)
    file_schem_xsd = models.FileField("Файл XML схемы (XSD)", upload_to='xml_schemas/', null=True, blank=True)
    file_annot = models.FileField("Файл аннотации (PDF)", upload_to='xml_schemas/', null=True, blank=True)
    date_public = models.DateField("Дата публикации", default=datetime.date.today)
    date_upload = models.DateField("Дата загрузки на сайт", default=datetime.date.today)
    date_unused = models.DateField("Дата прекращения использования", default=datetime.date.today)
    version = models.CharField("Версия XML", max_length=20, null=True, blank=True)
    normative = models.CharField("Норматив", max_length=1000, null=True, blank=True)
    link = models.CharField("Ссылка", max_length=1000, null=True, blank=True)
    ai_model = models.ForeignKey('AI_Models', verbose_name="Модель для преобразования", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "XML схема"  
        verbose_name_plural = "XML схемы"  
    
    @classmethod
    def get_schema_choices(cls):
        # Возвращаем выборку схем
        return cls.objects.values_list('id', 'name')



class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)


