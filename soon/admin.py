from django.contrib import admin
from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name' , 'subject']
	list_filter = ('name' , 'date')

@admin.register(Article)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name' , 'category']
	list_filter = ('like' , 'date')
