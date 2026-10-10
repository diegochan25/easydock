from django.urls import include, path
from apps.projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/services', include('apps.services.urls'))
]
