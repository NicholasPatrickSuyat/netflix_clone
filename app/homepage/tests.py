from django.test import TestCase
from django.urls import reverse
from homepage.models import Homepage
import pytest

# Create your tests here.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.fixture
def homepage_about(db):
    homepage = Homepage.objects.create(
        title='Pytest Homepage',
        homepage_url='http://127.0.0.1:8000',
        description='This is the Homepage!',
        published=True
    )
    return homepage

def test_homepage_title(homepage_about):
    assert Homepage.objects.filter(title='Pytest Homepage').exists()

def test_homepage_url(homepage_about):
    assert Homepage.objects.filter(homepage_url='http://127.0.0.1:8000').exists()