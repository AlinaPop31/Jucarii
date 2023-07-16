from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class Categorie(models.Model):
    nume = models.CharField(max_length=128)
    def __str__(self):
        return self.nume




class Jucarie(models.Model):
    nume = models.CharField(max_length=128)
    categorii = models.ManyToManyField(Categorie)
    varsta = models.IntegerField()
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.nume







