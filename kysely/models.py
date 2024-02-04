from django.db import models


class Kysymys(models.Model):
    kysymysteksti = models.CharField(max_length=200)
    julkaisupvm = models.DateTimeField("julkaistu")


class Vaihtoehto(models.Model):
    kysymys = models.ForeignKey(Kysymys, on_delete=models.CASCADE)
    teksti = models.CharField(max_length=200)
    aania = models.IntegerField(default=0)