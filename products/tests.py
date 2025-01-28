from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Product, Category

class ProductViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='admin', password='password')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(name='Test Product', price=10.00, category=self.category)
        self.all_products_url = reverse('products')
        self.product_detail_url = reverse('product_detail', args=[self.product.id])
        self.add_product_url = reverse('add_product')
        self.edit_product_url = reverse('edit_product', args=[self.product.id])
        self.delete_product_url = reverse('delete_product', args=[self.product.id])

    def test_all_products_view(self):
        response = self.client.get(self.all_products_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertContains(response, 'Test Product')

    def test_product_detail_view(self):
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertContains(response, 'Test Product')

    def test_add_product_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(self.add_product_url, {
            'name': 'New Product',
            'price': 20.00,
            'category': self.category.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product_detail', args=[Product.objects.last().id]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully added product!')

    def test_edit_product_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(self.edit_product_url, {
            'name': 'Updated Product',
            'price': 15.00,
            'category': self.category.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product_detail', args=[self.product.id]))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully updated product!')

    def test_delete_product_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(self.delete_product_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.all_products_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Product deleted!')
