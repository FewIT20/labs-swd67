from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class DoctorList(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

class PatientList(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

class AppintmentDetailList(APIView):
    
    def get(self, request, pk):
        appointments = Appointment.objects.get(pk=pk)
        if not appointments:
            return Response({"message": "No appointments found for this doctor."})
        serializer = AppointmentSerializer(appointments)
        return Response(serializer.data)
    
    def put(self, request, pk):
        appointments = Appointment.objects.get(pk=pk)
        if not appointments:
            return Response({"message": "No appointments found for this doctor."})
        serializer = UpdateAppointmentSerializer(appointments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def patch(self, request, pk):
        appointments = Appointment.objects.get(pk=pk)
        if not appointments:
            return Response({"message": "No appointments found for this doctor."})
        serializer = UpdateAppointmentSerializer(appointments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        appointments = Appointment.objects.get(pk=pk)
        if not appointments:
            return Response({"message": "No appointments found for this doctor."})
        appointments.delete()
        return Response({"message": "Appointment deleted successfully."})
        

class AppointmentList(APIView):
    
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UpdateAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)