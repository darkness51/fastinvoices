from django.db import models
from datetime import datetime
from django_countries import CountryField
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Category(models.Model):
    '''
    Class for categories
    '''
    name = models.CharField(_("Category Name"), max_length=255)
    parent = models.ForeignKey('self', null=True, verbose_name=_('parent'))
    reference = models.IntegerField(_('Reference'))
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    
class Tax(models.Model):
    '''
    Class for Taxes
    '''
    
    TYPES = (
        (u'QTY', _('Quantity')),
        (u'PER', _('Percentaje')),
    )
    
    name = models.CharField(_('Tax Name'), max_length=255)
    tax_type = models.CharField(verbose_name=_("Type"), max_length=4, choices=TYPES, default='PER')
    rate = models.FloatField(_('Rate'))
    active = models.BooleanField(_('Active'), default=True)
    
    class Meta:
        verbose_name = _('Tax')
        verbose_name_plural = _('Taxes')

class Product(models.Model):
    '''
    Class to represent a product
    '''
    code = models.CharField(_('Code'), max_length=255)
    item = models.CharField(_('Item'), max_length=255)
    category = models.ForeignKey(Category, verbose_name=_('Cateogory'))
    price_unit = models.FloatField(_('Price Unit'))
    cost_unit = models.FloatField(_('Cost Unit'))
    taxes = models.ForeignKey(Tax, verbose_name=_('Taxes'))
    description = models.TextField(_('Description'))
    active = models.BooleanField(_('Active'), default=True)
    
    def __unicode__(self):
        return "%s" % self.code
    
class CustomAttribute(models.Model):
    '''
    Class for custom fields in products
    '''
    product = models.ForeignKey(Product)
    name = models.CharField(_('Name'), max_length=255)
    value = models.CharField(_('Value'), max_length=255)
    
    def __unicode__(self):
        return "%s: %s" % (self.name, self.value)
        
class Client(models.Model):
    '''
    Class for clients
    '''
    name = models.CharField(verbose_name=_("Client Name"), max_length=255)
    contact = models.CharField(_('Contact'), max_length=255) # Change this for a foreign key??
    address = models.CharField(_('Address'), max_length=255)
    city = models.CharField(_('City'), max_length=150)
    zip_code = models.IntegerField(_('Zip Code'))
    state = models.CharField(_('State'), max_length=255)
    country = CountryField()
    phone = models.CharField(_('Phone'), max_length=20)
    cellphone = models.CharField(_('Cellphone'), max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField()
    entity_name = models.CharField(_('Entity Name'), max_length=255)
    business_id = models.CharField(_('Bussines ID'), max_length=50)
    tax_id = models.CharField(_('Tax ID'), max_length=20)
    tax_address = models.TextField(_('Tax Address'))
    line_of_bussiness = models.CharField(_('Line of Business'), max_length=255)
    observations = models.TextField(_('Observations'))
    active = models.BooleanField(_('Active'), default=True)
    
    def __unicode__(self):
        return "%s" % self.name
    