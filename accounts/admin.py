from django.contrib import admin

# Register your models here.
from .models import accounts
from .models import records

admin.site.register(accounts)
admin.site.register(records)
