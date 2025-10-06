"""
Endpoint tests for the Django application.
"""

import pytest
from django.test import TestCase, Client
from django.urls import reverse


class HelloWorldEndpointTest(TestCase):
    """Test suite for hello_world endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    @pytest.mark.timeout(30)
    def test_hello_world_endpoint(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.hello_world

        Test that the hello_world endpoint returns a successful response
        and renders the correct template with expected content.
        """
        # Get the URL for the hello_world view
        url = reverse('hello_world')

        # Make a GET request to the endpoint
        response = self.client.get(url)

        # Assert the response is successful
        self.assertEqual(response.status_code, 200)

        # Assert the correct template is used
        self.assertTemplateUsed(response, 'django_app/hello.html')

        # Assert the response contains expected content
        self.assertContains(response, 'Hello from CodeSpeak!')
        self.assertContains(response, 'Welcome to your new Django application')
        self.assertContains(response, 'Powered by Django')

        # Assert content type is HTML
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')