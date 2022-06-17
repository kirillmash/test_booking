from django.test import TestCase
from django.urls import reverse

from reservation.models import Rental, Reservation


class ReservationTestCase(TestCase):

    def setUp(self) -> None:
        self.rental1 = Rental.objects.create(name='Test Rental 1')
        self.rental2 = Rental.objects.create(name='Test Rental 2')

        self.reservation1 = Reservation.objects.create(rental=self.rental1, checkin='2020-01-01', checkout='2020-01-02')
        self.reservation2 = Reservation.objects.create(rental=self.rental1, checkin='2020-01-03', checkout='2020-01-04')
        self.reservation3 = Reservation.objects.create(rental=self.rental1, checkin='2020-01-05', checkout='2020-01-06')

        self.reservation4 = Reservation.objects.create(rental=self.rental2, checkin='2020-01-07', checkout='2020-01-08')
        self.reservation5 = Reservation.objects.create(rental=self.rental2, checkin='2020-01-09', checkout='2020-01-10')

    def test_reservation_list(self):
        expected_data = [
            {
                'id': self.reservation1.id,
                'rental_name': self.rental1.name,
                'checkin': '2020-01-01',
                'checkout': '2020-01-02',
                'previous_reservation': None,
            },
            {
                'id': self.reservation2.id,
                'rental_name': self.rental1.name,
                'checkin': '2020-01-03',
                'checkout': '2020-01-04',
                'previous_reservation': self.reservation1.id,
            },
            {
                'id': self.reservation3.id,
                'rental_name': self.rental1.name,
                'checkin': '2020-01-05',
                'checkout': '2020-01-06',
                'previous_reservation': self.reservation2.id,
            },
            {
                'id': self.reservation4.id,
                'rental_name': self.rental2.name,
                'checkin': '2020-01-07',
                'checkout': '2020-01-08',
                'previous_reservation': None,
            },
            {
                'id': self.reservation5.id,
                'rental_name': self.rental2.name,
                'checkin': '2020-01-09',
                'checkout': '2020-01-10',
                'previous_reservation': self.reservation4.id,
            },
        ]

        url = reverse('reservation:reservation-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
