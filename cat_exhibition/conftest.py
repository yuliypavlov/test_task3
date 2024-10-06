import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from api.models import Breed, Cat

User = get_user_model()


@pytest.fixture
def user(db):
    """
    Fixture for creating a user for testing.
    """
    return User.objects.create_user(username='user', password='password')


@pytest.fixture
def user2(db):
    """
    Fixture for creating a user2 for testing.
    """
    return User.objects.create_user(username='user2', password='password')


@pytest.fixture
def authenticated_client(user):
    """
    Fixture for creating an authenticated APIClient for testing.
    """
    client = APIClient()
    client.force_authenticate(user)
    return client


@pytest.fixture
def authenticated_client2(user2):
    """
    Fixture for creating an authenticated APIClient2 for testing.
    """
    client = APIClient()
    client.force_authenticate(user2)
    return client


@pytest.fixture
def breed(db):
    """
    Fixture for creating a breed for testing.
    """
    return Breed.objects.create(name='Siamese', description='Fluffy')


@pytest.fixture
def cat(breed, user):
    """
    Fixture for creating a cat dictionary for testing.
    """
    cat = {'breed': breed,
           'owner': user,
           'color': 'black',
           'age': 3,
           'description': 'Fluffy'}
    return cat


@pytest.fixture
def cat_obj(breed, user):
    """
    Fixture for creating a cat instance for testing.
    """
    return Cat.objects.create(breed=breed,
                              owner=user,
                              color='black',
                              age=3,
                              description='Fluffy')


@pytest.fixture
def rating(cat_obj):
    """
    Fixture for creating a rating dictionary for testing.
    """
    rating = {'cat': cat_obj.id, 'rating': 5}
    return rating


@pytest.fixture
def rating2(cat_obj):
    """
    Fixture for creating another rating dictionary for testing.
    """
    rating = {'cat': cat_obj.id, 'rating': 4}
    return rating
