from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status

class CategoriaTestCase(APITestCase):

    url = '/categorias/'

    def test_get_categoria(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_categoria_filter_exceeds_limit(self):
        url = self.url + '?filter=exceeds-limit'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_categoria_filter_not_exceeds_limit(self):
        url = self.url + '?filter=not-exceeds-limit'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_categoria(self): 
        response = self.client.post(self.url, 
        {
            "name": "Tecnología",
            "limit": "1500",
        },)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_categoria(self): 
        post = self.client.post(self.url, 
        {
            "name": "Tecnología",
            "limit": "1500",
        },)

        url = self.url + str(post.data["id"]) + '/'
        response = self.client.put(url, 
        {
            "name": "Tecnología",
            "limit": "2000",
        },)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_categoria(self): 
        post = self.client.post(self.url, 
        {
            "name": "Tecnología",
            "limit": "1500",
        },)

        url = self.url + str(post.data["id"]) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TransaccionTestCase(APITestCase):

    url = '/transacciones/'

    def test_get_transaccion(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_transaccion(self):
        categoria = self.client.post('/categorias/', 
        {
            "name": "Tecnología",
            "limit": "1500",
        },)

        response = self.client.post(self.url, 
        {
            "description": "Falabella",
            "amount": 350,
            "date": "2023-05-20",
            "ignore": False,
            "category": categoria.data["id"],
        },)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_put_transaccion(self):
        categoria = self.client.post('/categorias/', 
        {
            "name": "Tecnología",
            "limit": "1500",
        },)

        post = self.client.post(self.url, 
        {
            "description": "Falabella",
            "amount": 350,
            "date": "2023-05-20",
            "ignore": False,
            "category": categoria.data["id"],
        },)

        url = self.url + str(post.data["id"]) + '/'

        response = self.client.put(url, 
        {
            "description": "Falabella",
            "amount": 500,
            "date": "2023-05-20",
            "ignore": False,
            "category": categoria.data["id"],
        },)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_transaccion(self):
        categoria = self.client.post('/categorias/', 
        {
            "name": "Tecnología",
            "limit": "1500",
        },)

        post = self.client.post(self.url, 
        {
            "description": "Falabella",
            "amount": 350,
            "date": "2023-05-20",
            "ignore": False,
            "category": categoria.data["id"],
        },)

        url = self.url + str(post.data["id"]) + '/'

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
