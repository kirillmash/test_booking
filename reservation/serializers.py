from rest_framework import serializers

from reservation.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):

    rental_name = serializers.CharField(source='rental.name')
    previous_reservation = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Reservation
        fields = (
            'id',
            'rental_name',
            'checkin',
            'checkout',
            'previous_reservation',
        )
