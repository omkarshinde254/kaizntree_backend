from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Category, Item
import json

class CategoryItemTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category_count_url = reverse('category-count')
        self.item_count_url = reverse('item-count')
        self.category_create_url = reverse('category-create')
        self.category_data = {
            "name": "test_category",
        }
        self.item_create_url = reverse('item-create')
        self.category_list_url = reverse('category-list')
        self.item_list_url = reverse('item-list')
        self.item_data = {
            "sku": "test_sku",
            "name": "test_item",
            "tags": "test_tags",
            "category": "test_category",
            "in_stock": "yes",
            "available": "yes"
        }

    def test_category_count(self):
        response = self.client.get(self.category_count_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_item_count(self):
        response = self.client.get(self.item_count_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        response = self.client.post(self.category_create_url, self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'test_category')

    # def test_create_item(self):
    #     response = self.client.post(self.category_create_url, self.category_data, format='json')
    #     response = self.client.post(self.item_create_url, self.item_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Item.objects.count(), 1)
    #     self.assertEqual(Item.objects.get().sku, 'test_sku')


    def test_category_list(self):
        response = self.client.get(self.category_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_item_list(self):
    #     self.test_create_item()  # Create an item first
    #     response = self.client.get(self.item_list_url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)