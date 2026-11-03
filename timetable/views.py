from django.shortcuts import render
from .models import TimeSlot

def timetable_list(request):
    # Make sure this uses .all() with parentheses to get the full list
    timetable = TimeSlot.objects.all() 
    
    return render(request, 'timetable/timetable.html', {'timetable': timetable})