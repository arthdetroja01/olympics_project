from django.contrib import admin
from django.db.models.functions import Lower
from .models import Nation, Fitness, CurrentPlayer
# Register your models here.

class NationAdmin(admin.ModelAdmin):
    list_display = ['nation', 'national_anthem']

class FitnessAdminView(admin.ModelAdmin):
    list_display = ['fitness_id', 'height', 'weight', 'doping_results']
    ordering = ['fitness_id']

class CurrentPlayerAdminView(admin.ModelAdmin):
    list_display = ['player_id', 'first_name', 'last_name', 'address', 'email', 'marital_status', 'gender', 'phone_number', 'dob', 'fitness_id', 'nation']

admin.site.register(Fitness, FitnessAdminView)
admin.site.register(Nation, NationAdmin)
admin.site.register(CurrentPlayer, CurrentPlayerAdminView)
