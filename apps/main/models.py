from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    '''
    Class for categories
    '''
    nombre = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
class Tax(models.Model):
    '''
    Class for Taxes
    '''
    
    TYPES = (
        (u'QTY', u'Quantity'),
        (u'PER', u'Percentaje'),
    )
    
    name = models.CharField(max_length=255)
    tax_type = models.CharField(verbose_name="Type", max_length=4, choices=TYPES, default='PER')
    rate = models.FloatField()
    active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Taxes'

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
    active = models.BooleanField(default=True)
    
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
    