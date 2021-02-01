from django.db import models


class Colleges(models.Model):
    """
    Manage Colleges
    """
    name = models.CharField(max_length=40)
    province = models.CharField(max_length=10)
    is_211 = models.BooleanField(default=False)
    is_985 = models.BooleanField(default=False)

    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"

    def __str__(self):
        return self.name
