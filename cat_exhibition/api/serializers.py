from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import Cat, Breed, Rating


class BreedSerializer(serializers.ModelSerializer):
    """
    Serializer for the Breed model.
    """
    class Meta:
        model = Breed
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    """
    Serializer for the Cat model.
    """
    owner = serializers.StringRelatedField(read_only=True)
    breed = serializers.SlugRelatedField(slug_field='name',
                                         queryset=Breed.objects.all())

    class Meta:
        model = Cat
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rating model.
    """
    user = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Rating
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Rating.objects.all(),
                fields=['cat', 'user']
            )
        ]
