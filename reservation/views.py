from django.db.models import Subquery, OuterRef
from rest_framework import generics

from reservation.models import Reservation
from reservation.serializers import ReservationSerializer


class ReservationListAPIView(generics.ListAPIView):
    """
    This view should return a list of all the reservations with extra field last reservation which is the same rental.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.all().select_related('rental').annotate(previous_reservation=Subquery(
            Reservation.objects.filter(
                rental=OuterRef('rental'),
                checkin__lt=OuterRef('checkin'),
            ).order_by('-checkin').values('pk')[:1]))
