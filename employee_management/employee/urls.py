from django.urls import path
from .views import ViewEmployee, ViewPosition, ViewProject, ViewProjectDetail, ViewLayout

urlpatterns = [
    path('', ViewEmployee.as_view(), name='employee'),
    path('layout/', ViewLayout.as_view(), name='layout'),
    path('position/', ViewPosition.as_view(), name='position'),
    path('project/', ViewProject.as_view(), name='project'),
    path('project/<int:id>/', ViewProjectDetail.as_view(), name='project_detail'),
]