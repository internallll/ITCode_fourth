from contextlib import nullcontext
from http.client import responses
from wsgiref.validate import assert_

from django.template.defaultfilters import title
from django.test import TestCase
from django.urls import reverse

from bas import factories, models


# Create your tests here.

class basTestCase(TestCase):

    def setUp(self):
        self.busPark = factories.BusParkFactory()

    def test_get_busPark_list(self):
        url = reverse('park_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['busPark'].count(), models.BusPark.objects.count())
        #print(response.context['busPark'].count(), models.BusPark.objects.count())

    def test_get_busPark_detail(self):
        url = reverse('park_detail', kwargs={'pk': self.busPark.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_busPark(self):
        url = reverse('park_update', kwargs={'pk': self.busPark.pk})
        old_title = self.busPark.title
        old_description = self.busPark.description

        response = self.client.post(url, {
            'title': 'Updated Park',
            'address': '456 New Address',
            'phone_number': '0987654321',
            'year_found': 2021,
            'description': 'Updated description'
        })

        self.busPark.refresh_from_db()

        self.assertEqual(self.busPark.title, 'Updated Park')
        self.assertEqual(self.busPark.address, '456 New Address')
        self.assertEqual(self.busPark.phone_number, '0987654321')
        self.assertEqual(self.busPark.year_found, 2021)
        self.assertEqual(self.busPark.description, 'Updated description')

        self.assertEqual(response.status_code, 302)


    def test_delete_busPark(self):
        url = reverse('park_delete', kwargs={'pk': self.busPark.pk})
        old_count =models.BusPark.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        print(old_count,models.BusPark.objects.count())

    def test_create_busPark(self):
        url = reverse('park_create')
        old_count_BusPark =models.BusPark.objects.count()
        response = self.client.post(url, {'title': 'new_title',
                                          'address': 'new_address', #Создал новый обьект с обязательными полями названия и адреса
                                          'phone_number': '',       # а эти поля можно не заполнять у них blank = true
                                          'year_found': '',
                                          'description': ''})
        self.assertEqual(response.status_code, 302)

        print(f' Create: old:{old_count_BusPark} new: {models.BusPark.objects.count()}') #видно, что создалась новая модель
        self.assertNotEqual(old_count_BusPark, models.BusPark.objects.count())