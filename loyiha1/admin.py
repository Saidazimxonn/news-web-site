from django.contrib import admin
from .models import Blog,Position,Users
# Register your models here.

admin.site.register(Blog)
admin.site.register(Users)
@admin.register(Position)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
