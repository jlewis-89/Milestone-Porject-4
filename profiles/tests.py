from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import UserProfile, Favorite
from products.models import Product
from checkout.models import Order

class ProfileViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.favorite = Favorite.objects.create(user=self.user, product=self.product)
        self.order = Order.objects.create(
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
        self.profile_url = reverse('profile')
        self.order_history_url = reverse('order_history', args=['order_number'])
        self.password_reset_url = reverse('password_reset')
        self.favorites_list_url = reverse('favorites_list')
        self.add_to_favorites_url = reverse('add_to_favorites', args=[self.product.id])
        self.remove_from_favorites_url = reverse('remove_from_favorites', args=[self.product.id])

    def test_profile_view_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Test User')

    def test_profile_view_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.profile_url, {
            'full_name': 'Updated User',
            'email': 'updated@example.com',
            'phone_number': '0987654321',
            'country': 'GB',
            'postcode': 'BS1 2AA',
            'town_or_city': 'Bristol',
            'address1': '456 Updated Street',
            'address2': '',
            'county': 'Bristol',
        })
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Profile updated successfully')

    def test_order_history_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.order_history_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, 'order_number')

    def test_password_reset_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.password_reset_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/password_reset.html')

    def test_favorites_list_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.favorites_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/favorites_list.html')
        self.assertContains(response, 'Test Product')

    def test_add_to_favorites_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.add_to_favorites_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Product added to favorites')

    def test_remove_from_favorites_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.remove_from_favorites_url)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Product removed from favorites')
