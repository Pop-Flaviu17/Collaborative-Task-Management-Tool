from django.contrib import admin
from .models import Board, List, Card


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner', 'created_at')
    search_fields = ('name', 'description')

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'board',  'created_at')
    search_fields = ('name', 'board')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'list' ,'due_date', 'created_at')
    search_fields = ('name', 'description', 'list' )




