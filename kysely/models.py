from django.db import models


class Kysymys(models.Model):
    kysymysteksti = models.CharField(max_length=200)
    julkaisupvm = models.DateTimeField("julkaistu")

    class Meta:
        verbose_name = "kysymys"
        verbose_name_plural = "kysymykset"

    def __str__(self):
        return self.kysymysteksti


class Vaihtoehto(models.Model):
    kysymys = models.ForeignKey(Kysymys, on_delete=models.CASCADE)
    teksti = models.CharField(max_length=200)
    aania = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Vaihtoehto"
        verbose_name_plural = "Vaihtoehdot"

    def __str__(self):
        return self.teksti