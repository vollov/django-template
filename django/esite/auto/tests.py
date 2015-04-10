from django.test import TestCase

from models import Car

class CarMethodTests(TestCase):

    def test_save_car(self):
        car = Car(make='Acura',model='TL', kilometers=74673, year=2012, color='White', engine_size=3.7, drivetrain='AWD', transmition='MA')
        car.save()
        
        self.assertEqual(car.drivetrain, 'AWD')
        self.assertEqual(car.transmition, 'MA')