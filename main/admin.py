from django.contrib import admin
from .models import Checklist, Item, ItemChecklist, ImagensChecklist
# Register your models here.

class ChecklistAdmin(admin.ModelAdmin):
    readonly_fields = ('date','title')
    
class testeAdmin(admin.ModelAdmin):
    readonly_fields = ('item',)

admin.site.register(Checklist,ChecklistAdmin)
admin.site.register(Item)
admin.site.register(ItemChecklist,)
admin.site.register(ImagensChecklist,)
