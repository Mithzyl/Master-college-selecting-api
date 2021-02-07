from django.utils import timezone
from django.db import models
from Users.models import User
from Majors.models import Majors
from Subjects.models import PoliticSubject, ForeignLanguageSubject,\
                                            FirstMajorSubject, SecondMajorSubject
from Colleges.models import Colleges


class FavoriteColleges(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base = models.ForeignKey(Colleges, on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Favorite College'
        verbose_name_plural = 'Favorite Colleges'

    def __str__(self):
        return str(self.base)


class FavoriteMajors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    base = models.ForeignKey(Majors, on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Favorite major'
        verbose_name_plural = 'Favorite majors'

    def __str__(self):
        return str(self.base)
