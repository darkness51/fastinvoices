from django.contrib import admin
from models import Category, Tax, Product, CustomAttribute, Client

class CustomAttributeInline(admin.TabularInline):
    model = CustomAttribute
    extra = 3
    
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Information", {'fields': ['code', 'item', 'category', 'active']}),
        ("Money", {'fields': ['price_unit', 'cost_unit', 'taxes']}),
        ("Description", {'fields': ['description']}),
    ]
    inlines = [CustomAttributeInline]

admin.site.register(Category)
admin.site.register(Tax)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client)