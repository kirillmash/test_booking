from django.urls import path

from reservation.views import ReservationListAPIView

app_name = 'reservation'

urlpatterns = [

    path('', ReservationListAPIView.as_view(), name='reservation-list'),

]
