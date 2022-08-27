from django.contrib.auth.models import User
from rest_framework import serializers

from ecomerce_app1.models import Products


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['id','name', 'image', 'description', 'colors', 'grade', 'rating', 'quality','size', 'created_by']


