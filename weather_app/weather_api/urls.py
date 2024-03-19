from django.urls import path
from . import views

urlpatterns = [
    path('meteo/get/', views.queryDataFromMeteo),
    path('daytemp/list/', views.listDayTempData),
    path('daytemp/create/', views.storeDayTempData),
    path('daytemp/read/<int:id>', views.readDayTempData),
    path('daytemp/update/<int:id>', views.updateDayTempData),
    path('daytemp/delete/<int:id>', views.deleteDayTempData),
]
