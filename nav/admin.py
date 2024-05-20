from django.contrib import admin
from .models import Category, Icon, App
# Register your models here.
# admin.site.register(Category)
admin.site.register(Icon)
admin.site.register(App)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'father')


admin.site.site_header='AI导航管理系统'
admin.site.site_title='AI导航管理系统'