from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from django.conf import settings
import json
import stripe

class CheckoutViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.user = UserProfile.objects.create(user=self.client)
        self.cart = {str(self.product.id): 1}
        self.client.session['cart'] = self.cart
        self.client.session.save()
        self.cache_checkout_data_url = reverse('cache_checkout_data')
        self.checkout_url = reverse('checkout')
        self.checkout_success_url = reverse('checkout_success', args=['order_number'])

    def test_cache_checkout_data(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=1000,
            currency=settings.STRIPE_CURRENCY,
        )
        response = self.client.post(self.cache_checkout_data_url, {
            'client_secret': intent.client_secret,
            'save_info': 'on',
        })
        self.assertEqual(response.status_code, 200)

    def test_checkout_view_get(self):
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_view_post(self):
        response = self.client.post(self.checkout_url, {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'country': 'GB',
            'postcode': 'BS1 1AA',
            'town_or_city': 'Bristol',
            'address1': '123 Test Street',
            'address2': '',
            'county': 'Bristol',
            'client_secret': 'test_client_secret',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('checkout_success', args=['order_number']))

    def test_checkout_success_view(self):
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='GB',
            postcode='BS1 1AA',
            town_or_city='Bristol',
            address1='123 Test Street',
            address2='',
            county='Bristol',
            order_number='order_number',
        )
        response = self.client.get(self.checkout_success_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Order successfully processed! Your order number is order_number. A confirmation email will be sent to test@example.com.')
