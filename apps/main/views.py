from models import *
from datetime import datetime
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404
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