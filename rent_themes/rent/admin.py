from django.contrib import admin

from.models import Client, Item, Theme
# Register your models here.

admin.site.register(Client)
admin.site.register(Theme)
admin.site.register(Item)