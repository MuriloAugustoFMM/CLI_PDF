from django.shortcuts import render
from .forms import NameForm

def index(request):

    return(render(
        request,
        'global/index.html'
    ))
