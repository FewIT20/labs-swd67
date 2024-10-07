from django.urls import path
from .views import DoctorList, PatientList, AppointmentList, AppintmentDetailList

urlpatterns = [
    path('doctors/', DoctorList.as_view(), name='doctor-list'),
    path('patients/', PatientList.as_view(), name='patient-list'),
    path('appointments/', AppointmentList.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppintmentDetailList.as_view(), name='appointment-detail-list'),
]