from django.db import models


class Majors(models.Model):
    """
    Manage majors
    """
    MAJOR_CHOICES = (
        ('专业学位', '专业学位'),
        ('学术学位', '学术学位'),
    )
    classes = models.CharField(max_length=10, choices=MAJOR_CHOICES)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Major'
        verbose_name_plural = 'Majors'

    def __str__(self):
        return self.name
