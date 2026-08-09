from django.contrib import admin

from .models import Country,Profile

admin.site.register(Country)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone_number','country','avatar')


