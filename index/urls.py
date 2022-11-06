from django.urls import path
from index import views

urlpatterns = [
    path('', views.ResultIndex, name='home'),
    path('lga/', views.get_lga, name='get_LGA')
]