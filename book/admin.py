from django.contrib import admin
from .models import Club, Court, Slot

# Register your models here.
admin.site.register(Club)
admin.site.register(Court)
admin.site.register(Slot)
