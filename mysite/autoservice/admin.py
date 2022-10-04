from django.contrib import admin
from .models import (AutomobilioModelis,
                     Automobilis,
                     Paslauga,
                     Uzsakymas,
                     UzsakymoEilute)


class UzsakymoEiluteInline(admin.TabularInline):
    model = UzsakymoEilute
    extra = 0


class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('automobilis', 'data')
    inlines = [UzsakymoEiluteInline]


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('modelis', 'valstybinis_nr', 'vin_kodas', 'kliento_vardas')
    list_filter = ('kliento_vardas', 'modelis')


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')


# Register your models here.
admin.site.register(AutomobilioModelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute)
