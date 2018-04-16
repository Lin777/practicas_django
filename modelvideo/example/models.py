from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20, default="USA")
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20, default='NaN')
    paradigm = models.CharField(max_length=20, default='NaN')
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=23)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name

