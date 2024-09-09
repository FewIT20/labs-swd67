from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewEmployee.as_view(), name='employee'),
    path('create/', ViewCreateEmployee.as_view(), name='create_employee'),
    path('layout/', ViewLayout.as_view(), name='layout'),
    path('position/', ViewPosition.as_view(), name='position'),
    path('project/', ViewProject.as_view(), name='project'),
    path('project/create', ViewProjectCreate.as_view(), name='create_project'),
    path('project/update/<int:id>/', UpdateProject.as_view(), name='update_project'),
    path('project/<int:id>/', ViewProjectDetail.as_view(), name='project_detail'),
]