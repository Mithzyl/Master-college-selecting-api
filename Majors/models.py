from django.db import models


class Majors(models.Model):
    """
    Manage majors
    """
    MAJOR_CHOICES = (
        (0, '专业学位'),
        (1, '学术学位'),
    )
    classes = models.BooleanField(choices=MAJOR_CHOICES)
    code = models.IntegerField()
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Major'
        verbose_name_plural = 'Majors'

    def __str__(self):
        return self.name
