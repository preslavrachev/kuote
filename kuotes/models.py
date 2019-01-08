from djongo import models


class Source(models.Model):
    url = models.URLField(verbose_name='Source URL')


class Kuote(models.Model):
    content = models.CharField(max_length=280)
    slug = models.TextField()
    source = models.EmbeddedModelField(model_container=Source)
