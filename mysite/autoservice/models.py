from django.db import models


# Create your models here.
class AutomobilioModelis(models.Model):
    gamintojas = models.CharField("Gamintojas", max_length=100)
    modelis = models.CharField("Modelis", max_length=100)


class Paslauga(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=200)
    kaina = models.FloatField("Kaina")


class Automobilis(models.Model):
    modelis = models.ForeignKey("AutomobilioModelis", on_delete=models.SET_NULL, null=True)
    valstybinis_nr = models.CharField("Valstybinis numeris", max_length=10)
    vin_kodas = models.CharField("VIN kodas", max_length=20)
    kliento_vardas = models.CharField("Kliento vardas", max_length=30)


class Uzsakymas(models.Model):
    data = models.DateField("Data", auto_now_add=True)
    automobilis = models.ForeignKey("Automobilis", on_delete=models.SET_NULL, null=True)


class UzsakymoEilute(models.Model):
    uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.CASCADE, null=True)
    paslauga = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis")
