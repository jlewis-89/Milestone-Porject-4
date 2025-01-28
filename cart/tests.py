from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Product

class CartViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name='Test Product', price=10.00)
        self.cart_url = reverse('cart')
        self.add_to_cart_url = reverse('add_to_cart', args=[self.product.id])
        self.adjust_cart_url = reverse('adjust_cart', args=[self.product.id])
        self.remove_from_cart_url = reverse('remove_from_cart', args=[self.product.id])

    def test_cart_view(self):
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart(self):
        response = self.client.post(self.add_to_cart_url, {
            'quantity': 1,
            'redirect_url': self.cart_url
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.cart_url)
        cart = self.client.session['cart']
        self.assertIn(str(self.product.id), cart)
        self.assertEqual(cart[str(self.product.id)], 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Added {self.product.name} to your cart')

    def test_adjust_cart(self):
        self.client.session['cart'] = {str(self.product.id): 1}
        self.client.session.save()
        response = self.client.post(self.adjust_cart_url, {
            'quantity': 2
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))
        cart = self.client.session['cart']
        self.assertEqual(cart[str(self.product.id)], 2)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Updated {self.product.name} quantity to 2')

    def test_remove_from_cart(self):
        self.client.session['cart'] = {str(self.product.id): 1}
        self.client.session.save()
        response = self.client.post(self.remove_from_cart_url)
        self.assertEqual(response.status_code, 200)
        cart = self.client.session['cart']
        self.assertNotIn(str(self.product.id), cart)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Removed {self.product.name} from your cart')
