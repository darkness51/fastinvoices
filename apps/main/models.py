from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    '''
    Class for categories
    '''
    nombre = models.CharField(max_length=255)
    
    
class Tax(models.Model):
    '''
    Class for Taxes
    '''
    name = models.CharField(max_length=255)

class Product(models.Model):
    '''
    Class to represent a product
    '''
    code = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    price_unit = models.FloatField()
    cost_unit = models.FloatField()
    taxes = models.ForeignKey(Tax)
    description = models.TextField()
    active = models.BooleanField()
    
    def __unicode__(self):
        return "%s" % self.code
    
class CustomAttribute(models.Model):
    '''
    Class for custom fields in products
    '''
    product = models.ForeignKey(Product)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    
    def __unicode__(self):
        return "%s: %s" % (self.name, self.value)
    