from django.db import models


class Majors(models.Model):
    """
    Manage majors
    """
    MAJOR_CHOICES = (
        (0, '学术学位'),
        (1, '专业学位'),
    )
    name = models.CharField(max_length=40)
    classes = models.IntegerField(choices=MAJOR_CHOICES)

    class Meta:
        verbose_name = 'Major'
        verbose_name_plural = 'Majors'

    def __str__(self):
        return self.name
