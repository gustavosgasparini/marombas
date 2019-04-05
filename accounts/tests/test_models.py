from django.test import TestCase
from accounts.models import User
from django.utils import timezone
import datetime
from unittest import mock
import pytz


class TestAccountsModels(TestCase):

    def setUp(self):
        self.new_user = User.object.create(
            pk=15,
            first_name='Gustavo',
            last_name='Gasparini',
            username='gustavo',
            email='gustavo@email.com',
            works_out='BlueFit',
            last_gym='SmartFit',
            city='Goiânia',
            hometown='Conchal',
            is_active=True,
            is_admin=False,
            is_staff=False,
        )

    def test_user_joined(self):
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            user = User.object.create(pk=25)
            self.assertEquals(user.date_joined, timezone.now())

    def test_informations_checking_if_right(self):
        self.assertEquals(self.new_user.first_name, 'Gustavo')
        self.assertEquals(self.new_user.last_name, 'Gasparini')
        self.assertEquals(self.new_user.username, 'gustavo')
        self.assertEquals(self.new_user.email, 'gustavo@email.com')
        self.assertEquals(self.new_user.works_out, 'BlueFit')
        self.assertEquals(self.new_user.last_gym, 'SmartFit')
        self.assertEquals(self.new_user.city, 'Goiânia')
        self.assertEquals(self.new_user.hometown, 'Conchal')

    def test_user_activity(self):
        self.assertEquals(self.new_user.is_active, True)
        self.assertEquals(self.new_user.is_admin, False)
        self.assertEquals(self.new_user.is_staff, False)
