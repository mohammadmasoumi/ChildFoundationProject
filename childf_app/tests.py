from django.test import TestCase

# Create your tests here.


class PaymentTestCase(TestCase):
    def setUp(self):
        print('setup for test ')

    def test_payment(self):
        print('Hello')