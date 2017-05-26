from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.view import generic

from .models import Song

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'composer/index.html'
    context_object_name = '
