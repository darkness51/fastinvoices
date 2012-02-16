from models import *
from datetime import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
from pprint import pprint

import logging

logger = logging.getLogger(__name__)

def index(request):
    '''
    Main view for the application
    '''
    
    return render_to_response("index.html", context_instance=RequestContext(request))
    
def logout_page(request):
    '''
    Finish the user session
    '''
    logout(request)
    response = redirect('main.views.index')
    return response