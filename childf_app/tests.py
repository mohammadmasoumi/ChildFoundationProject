from django.test import TestCase

import datetime
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from .models import *
from .admin import MadadJouAdmin, MadadKarAdmin, HamYarAdmin

class RegistarationTestCase(TestCase):

    def test_Hamyar_Registration(self):
        hm = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        hm.save()
        x = HamYar.objects.get(username = 'ostad')
        self.assertEqual(x.username , 'ostad')
        self.assertEqual(x.password , '12345')
        self.assertEqual(x.email , 'ostad@nomre.khoob')

    def test_Madaju_Registration(self):
        group4 = MadadJou(user_id= 1 , niaz_mahane= 100, name='group4')
        group4.save()
        x = MadadJou.objects.get(user_id=1)
        self.assertEqual(x.name, 'group4')
        self.assertEqual(x.niaz_mahane,100)

class DataEdit(TestCase):

    def test_Hamyar_data_edit(self):
        hm = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        hm.save()
        hm.email = 'newEmail@nomre.khoob'
        hm.save()
        x = HamYar.objects.get(username='ostad')
        self.assertEqual(x.username, 'ostad')
        self.assertEqual(x.password, '12345')
        self.assertEqual(x.email, 'newEmail@nomre.khoob' )

    def test_Madaju_data_edit(self):
        group4 = MadadJou(user_id=1, niaz_mahane=100, name='group4')
        group4.save()
        MadadJou.name = 'poorGroup4'
        MadadJou.niaz_mahane = 200
        group4.save()
        x = MadadJou.objects.get(user_id=1)
        self.assertEqual(x.name, 'group4')
        self.assertEqual(x.niaz_mahane, 200)


class PaymentTest(TestCase):

    def test_payment(self):
        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()
        pdate = datetime.datetime.now() + datetime.timedelta(days = -30)
        payment = IPayment(amount=20, payer=ostad,date=pdate)
        payment.save()
        x = IPayment.objects.get(payer = ostad)
        self.assertEqual(x.amount,payment.amount)

class HelpReqTest(TestCase):

    def test_helpVerification(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()
        h = HelpRequest(madadjou=group4, amount=20)
        h.save()
        self.assertFalse(h.is_verified)

    def test_helpCritical(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()
        h = HelpRequest(madadjou=group4, amount=20)
        h.save()
        self.assertFalse(h.critical)

    def test_Verify(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()
        h = HelpRequest(madadjou=group4, amount=20)
        h.save()
        h.is_verified = True
        h.save()
        self.assertTrue(h.is_verified)

    def test_Verify_AnnounceCrtical(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()
        h = HelpRequest(madadjou=group4, amount=20)
        h.save()
        h.critical = True
        h.save()
        self.assertTrue(h.critical)

    def test_helpAfterPaymentPaySum(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()
        h = HelpRequest(madadjou=group4, amount=20)
        h.save()

        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()

        pdate = datetime.datetime.now() + datetime.timedelta(days = -30)
        payment = IPayment(amount=15, payer=ostad,date=pdate)
        payment.save()

        mp = MadadPayment(help_request=h,IPayment = payment)
        mp.save()

        self.assertEqual(h.payed_sum,15)

    def test_helpAfterPaymentRemaining(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()
        h = HelpRequest(madadjou=group4, amount=20)
        h.save()

        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()

        pdate = datetime.datetime.now() + datetime.timedelta(days=-30)
        payment = IPayment(amount=15, payer=ostad, date=pdate)
        payment.save()

        mp = MadadPayment(help_request=h, IPayment=payment)
        mp.save()

        self.assertEqual(h.needed, 5)


class MessageTests(TestCase):

    def test_create_messageMadadju2Hamyar(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()

        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()

        m = Message(sender=group4,receiver=ostad,subject='darkhaste nomre',body='Ostad to ro khoda nomre bede')
        m.save()
        x=Message.objects.get(sender=group4)
        self.assertEqual(x.body,m.body)
        self.assertEqual(x.subject,m.subject)

    def test_create_messageHamyar2Madaju(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()

        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()

        m = Message(sender=ostad, receiver=group4, subject='darkhaste nomre', body='Taid mishavad')
        m.save()
        x = Message.objects.get(receiver=group4)
        self.assertEqual(x.body, m.body)
        self.assertEqual(x.subject, m.subject)

    def test_create_messageMadadju2Madadkar(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()

        tau = User(username='TAKhoob',password='IAmGoodTA')
        ta = MadadKar(user=tau)

        m = Message(sender=group4, receiver=tau, subject='darkhaste nomre', body='Ostad to ro khoda nomre bede')
        m.save()
        x = Message.objects.get(sender=group4)
        self.assertEqual(x.body, m.body)
        self.assertEqual(x.subject, m.subject)

    def test_create_messageMadadkar2Madadkar(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()

        tau = User(username='TAKhoob',password='IAmGoodTA')
        tau.save()
        ta = MadadKar(user=tau)
        ta.save()

        m = Message(sender=ta, receiver=group4, subject='darkhaste nomre', body='Hatman!')
        m.save()
        x = Message.objects.get(sender=ta)
        self.assertEqual(x.body, m.body)
        self.assertEqual(x.subject, m.subject)

    def test_create_messageMadadkar2Hamyar(self):

        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()

        tau = User(username='TAKhoob',password='IAmGoodTA')
        tau.save()
        ta = MadadKar(user=tau)
        ta.save()

        m = Message(sender=ta, receiver=ostad, subject='darkhaste nomre', body='Hatman!')
        m.save()
        x = Message.objects.get(sender=ta)
        self.assertEqual(x.body, m.body)
        self.assertEqual(x.subject, m.subject)

    def test_create_messageHamyar2Madadkar(self):
        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()

        tau = User(username='TAKhoob', password='IAmGoodTA')
        tau.save()
        ta = MadadKar(user=tau)
        ta.save()

        m = Message(sender=ostad, receiver=ta, subject='darkhaste nomre', body='Hatman!')
        m.save()
        x = Message.objects.get(sender=ostad)
        self.assertEqual(x.body, m.body)
        self.assertEqual(x.subject, m.subject)

class LoginTest(TestCase):

    def test_Hamyar_Login(self):
        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()

        x = HamYar.objects.get(user_id = ostad.user_id)
        self.assertEqual(x.password,ostad.password)

    def test_Madadkar_Login(self):
        tau = User(username='TAKhoob', password='IAmGoodTA')
        tau.save()
        ta = MadadKar(user=tau)
        ta.save()

        x = MadadKar.objects.get(username=tau.username)

        self.assertEqual(x.password,tau.password)

    def test_MadadJou_Login(self):
        group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
        group4.save()

        x = MadadKar.objects.get(user_id=group4.user_id)
        self.assertEqual(x.password,tau.password)


class AdminTests(TestCase):

    def test_Hamyars(self):
        ostad = HamYar(username='ostad', password='12345', email='ostad@nomre.khoob', gender=1, education=2)
        ostad.save()

        x = HamYarAdmin.list_display
        self.assertEqual(x[0],ostad.username)

    # def test_Madadju(self):
    #     group4 = MadadJou(user_id=1, niaz_mahane=20, name='group4')
    #     group4.save()