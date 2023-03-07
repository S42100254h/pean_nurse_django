from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.model = User.objects.create(name='dummy', email='dummy@example.com')

    def test_create(self):
        data = {'name': 'neko', 'email': 'neko@gmail.com'}
        url = reverse('user-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(id=response.data['id']).name, 'neko')
        
