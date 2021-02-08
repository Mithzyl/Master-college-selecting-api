from django.utils import timezone
from django.db import models
from Users.models import User
from Majors.models import Majors
from Subjects.models import PoliticSubject, ForeignLanguageSubject,\
                                            FirstMajorSubject, SecondMajorSubject
from Colleges.models import Colleges


class FavoriteColleges(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    base = models.ForeignKey(Colleges, on_delete=models.CASCADE, related_name='colleges_name')
    add_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Favorite College'
        verbose_name_plural = 'Favorite Colleges'
        unique_together = ['base']

    def __str__(self):
        return "{}".format(self.base)


class FavoriteMajors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_for_majors')
    base = models.ForeignKey(Majors, on_delete=models.CASCADE, related_name='majors_name')
    add_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Favorite Major'
        verbose_name_plural = 'Favorite Majors'
        unique_together = ['base']

    def __str__(self):
        return "{}".format(self.base)
