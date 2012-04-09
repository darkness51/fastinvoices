from models import *
from datetime import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from pprint import pprint

import logging

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = "index.html"
    
class ProductListView(ListView):
    model = Product
    paginate_by = 10
    
class ProductAddView(CreateView):
    model = Product
        
def logout_page(request):
    '''
    Finish the user session
    '''
    logout(request)
    response = redirect('main.views.index')
    return response