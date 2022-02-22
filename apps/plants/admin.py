from django.contrib import admin
from .models import Plant, PlantedTree

admin.site.register(Plant)

@admin.register(PlantedTree)
class PlantedTreeAdmin(admin.ModelAdmin):
    model = PlantedTree
    list_display = ('tree', 'user', 'get_age')
    list_filter = ('tree', 'user')

    def get_age(self, obj):
        return obj.get_age()

    get_age.short_description = 'age'
