from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
  
def mobile(request):
    return render(request, 'draw/mobile.html', {})

def large(request):
    return render(request, 'draw/large.html', {})
  
def scanqr(request):
    return render(request, 'draw/scanqr.html', {})
