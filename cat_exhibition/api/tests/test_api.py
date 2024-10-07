import pytest
from django.urls import reverse
from rest_framework import status

from api.models import Cat, Rating


@pytest.mark.django_db
def test_create_cat(authenticated_client, cat):
    """
    Test the creation of a new cat.
    """
    url = reverse('cat-list')

    response = authenticated_client.post(url, cat)

    assert response.status_code == status.HTTP_201_CREATED
    assert Cat.objects.count() == 1


@pytest.mark.django_db
def test_cat_filter_by_breed(authenticated_client, breed):
    """
    Test filtering cats by breed.
    """
    url = reverse('cat-list')
    url_with_query = f'{url}?breed={breed.id}'

    response = authenticated_client.get(url_with_query)

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_rating(authenticated_client, rating):
    """
    Test the creation of a new breed.
    """
    url = reverse('rating-list')

    response = authenticated_client.post(url, rating)

    assert response.status_code == status.HTTP_201_CREATED
    assert Rating.objects.count() == 1


@pytest.mark.django_db
def test_unique_rating_per_user(authenticated_client, rating, rating2):
    """
    Test unique rating constraint per user.
    """
    url = reverse('rating-list')

    response1 = authenticated_client.post(url, rating)

    assert response1.status_code == status.HTTP_201_CREATED

    response2 = authenticated_client.post(url, rating2)

    assert response2.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_user_cant_modify_other_users_cat(authenticated_client2, cat_obj):
    """
    Test that a user can't modify another user's cat.
    """
    url = reverse('cat-detail', kwargs={'pk': cat_obj.id})

    response = authenticated_client2.patch(url, {'color': 'grey'})

    assert response.status_code == status.HTTP_403_FORBIDDEN
