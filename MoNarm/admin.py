from django.contrib import admin
from MoNarm.models import Article, Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['publish', 'status']


admin.site.register(Article, DataAdmin)
admin.site.register(Data, DataAdmin)
