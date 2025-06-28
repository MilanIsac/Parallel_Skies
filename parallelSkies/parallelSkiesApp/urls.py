from django.urls import path
from .views import views
# from .views.views import weather_prediction_view

urlpatterns = [
    path('', views.weather_view, name='weather_view'),
    # path('', weather_prediction_view, name='predict'),
]
