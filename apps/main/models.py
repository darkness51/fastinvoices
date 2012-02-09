from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    '''
    Class for categories
    '''
    nombre = models.CharField(max_length=255)
    #parent = models.ForeignKey(self)
    reference = models.IntegerField()
    
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
        
class Country(models.Model):
    '''
    Countries Table
    '''
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)
        
class Client(models.Model):
    '''
    Class for clients
    '''
    name = models.CharField(verbose_name="Client Name", max_length=255)
    contacto = models.CharField(max_length=255) # Se puede cambiar por un diccionario
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=150)
    zip_code = models.IntegerField()
    state = models.CharField(max_length=255)
    country = models.ForeignKey(Country)
    phone = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField()
    entity_name = models.CharField(max_length=255)
    business_id = models.CharField(max_length=50)
    tax_id = models.CharField(max_length=20)
    tax_address = models.TextField()
    line_of_bussiness = models.CharField(max_length=255)
    observations = models.TextField()
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "%s" % self.name
    