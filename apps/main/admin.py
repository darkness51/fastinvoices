from django.contrib import admin
from models import Category, Tax, Product, CustomAttribute

admin.site.register(Category)
admin.site.register(Tax)
admin.site.register(Product)
admin.site.register(CustomAttribute)