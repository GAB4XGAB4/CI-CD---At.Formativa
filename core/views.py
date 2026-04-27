from django.shortcuts import render
from .models import Note

def home(request):
    notes = Note.objects.all()
    return render(request, 'core/home.html', {'notes': notes})
