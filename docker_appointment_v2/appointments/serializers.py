from rest_framework import serializers
from .models import Doctor, Patient, Appointment
from datetime import datetime

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "phone_number",
            "email"
        ]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "phone_number",
            "email",
            "address"
        ]
        
class UpdateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "doctor",
            "patient",
            "date",
            "at_time",
            "details"
        ]
    
    def validate(self, data):
        date = data.get("date")
        at_time = data.get("at_time")
        
        combine = datetime.combine(date, at_time)
        if combine < datetime.now():
            raise serializers.ValidationError("The appointment date or time must be in the future.")
        
        return data
        
class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()
    
    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "patient",
            "date",
            "at_time",
            "details"
        ]