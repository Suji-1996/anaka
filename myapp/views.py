from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def calculate_oee(request, machine_id):
    try:
        machine = Machine.objects.get(pk=machine_id)
        production_logs = ProductionLog.objects.filter(machine=machine)
        total_production_time = sum(log.duration for log in production_logs)

        planned_production_time = total_production_time
        ideal_cycle_time = 1  # Assuming one cycle per hour

        availability = total_production_time / planned_production_time
        performance = total_production_time / (len(production_logs) * ideal_cycle_time)
        quality = 1  # Assuming perfect quality

        oee = availability * performance * quality

        return Response({'oee': oee})
    except Exception as e:
        return Response({'error': str(e)})

