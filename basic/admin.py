from django.contrib import admin
from .models import Blog, Profile, Clues


# Register your models here.
admin.site.register(Blog)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'clue_solved')
    
admin.site.register(Profile, ProfileAdmin)


class CluesAdmin(admin.ModelAdmin):
    list_display = ('location', 'clue', 'solved')
    
admin.site.register(Clues, CluesAdmin)