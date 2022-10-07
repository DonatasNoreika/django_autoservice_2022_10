from django.db import models


# Create your models here.
class AutomobilioModelis(models.Model):
    gamintojas = models.CharField("Gamintojas", max_length=100)
    modelis = models.CharField("Modelis", max_length=100)

    def __str__(self):
        return f"{self.gamintojas} {self.modelis}"

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilio modeliai"

class Paslauga(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=200)
    kaina = models.FloatField("Kaina")

    def __str__(self):
        return f"{self.pavadinimas}"

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"

class Automobilis(models.Model):
    modelis = models.ForeignKey("AutomobilioModelis", on_delete=models.SET_NULL, null=True)
    valstybinis_nr = models.CharField("Valstybinis numeris", max_length=10)
    vin_kodas = models.CharField("VIN kodas", max_length=20)
    kliento_vardas = models.CharField("Kliento vardas", max_length=30)
    photo = models.ImageField('Nuotrauka', upload_to='automobiliai', null=True)

    def __str__(self):
        return f"{self.modelis} {self.valstybinis_nr} ({self.kliento_vardas})"

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"
        ordering = ['-id']

class Uzsakymas(models.Model):
    data = models.DateField("Data")
    automobilis = models.ForeignKey("Automobilis", on_delete=models.SET_NULL, null=True, related_name="uzsakymai")

    def bendra(self):
        bendra = 0
        eilutes = self.eilutes.all()
        for eilute in eilutes:
            bendra += eilute.kiekis * eilute.paslauga.kaina
        return bendra

    STATUS = (
        ("p", "Patvirtinta"),
        ("v", "Vykdoma"),
        ("i", "Įvykdyta"),
        ("a", "Atšaukta"),
    )


    statusas = models.CharField(max_length=1, choices=STATUS, default="p", help_text="Statusas")

    def __str__(self):
        return f"{self.data} {self.automobilis}"

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"
        ordering = ['-id']


class UzsakymoEilute(models.Model):
    uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.CASCADE, null=True, related_name="eilutes")
    paslauga = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis")

    def suma(self):
        return self.kiekis * self.paslauga.kaina

    def __str__(self):
        return f"{self.uzsakymas} {self.paslauga} {self.kiekis}"

    class Meta:
        verbose_name = "Užsakyta paslauga"
        verbose_name_plural = "Užsakytos paslaugos"
