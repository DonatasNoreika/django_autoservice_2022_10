from django.db import models


# Create your models here.
class AutomobilioModelis(models.Model):
    gamintojas = models.CharField("Gamintojas", max_length=100)
    modelis = models.CharField("Modelis", max_length=100)

    def __str__(self):
        return f"{self.gamintojas} {self.modelis}"

class Paslauga(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=200)
    kaina = models.FloatField("Kaina")

    def __str__(self):
        return f"{self.pavadinimas}"

class Automobilis(models.Model):
    modelis = models.ForeignKey("AutomobilioModelis", on_delete=models.SET_NULL, null=True)
    valstybinis_nr = models.CharField("Valstybinis numeris", max_length=10)
    vin_kodas = models.CharField("VIN kodas", max_length=20)
    kliento_vardas = models.CharField("Kliento vardas", max_length=30)

    def __str__(self):
        return f"{self.modelis} {self.valstybinis_nr} ({self.kliento_vardas})"

class Uzsakymas(models.Model):
    data = models.DateField("Data")
    automobilis = models.ForeignKey("Automobilis", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.data} {self.automobilis}"


class UzsakymoEilute(models.Model):
    uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.CASCADE, null=True)
    paslauga = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis")

    def __str__(self):
        return f"{self.uzsakymas} {self.paslauga} {self.kiekis}"
