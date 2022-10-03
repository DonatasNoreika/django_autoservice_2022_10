from django.contrib import admin
from .models import (AutomobilioModelis,
                     Automobilis,
                     Paslauga,
                     Uzsakymas,
                     UzsakymoEilute)

# Register your models here.
admin.site.register(AutomobilioModelis)
admin.site.register(Automobilis)
admin.site.register(Paslauga)
admin.site.register(Uzsakymas)
admin.site.register(UzsakymoEilute)
