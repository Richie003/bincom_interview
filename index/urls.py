from django.urls import path
from index import views

urlpatterns = [
    path('', views.ResultIndex, name='home'),
    path('lga/', views.get_lga, name='get_LGA'),
    path('Party-result/', views.PartyIndex, name='PartyResult'),
    path('add-party-result/', views.addPartyResult, name='apres')
]