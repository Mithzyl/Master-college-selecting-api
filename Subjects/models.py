from django.db import models


class PoliticSubject(models.Model):
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ForeignLanguageSubject(models.Model):
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class FirstMajorSubject(models.Model):
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class SecondMajorSubject(models.Model):
    code = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=40)



    def __str__(self):
        return self.name
