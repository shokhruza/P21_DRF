from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.models import Product, Category, User


class RegisterUserModelSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'username', 'password', 'confirm_password'

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        if confirm_password != attrs.get('password'):
            raise serializers.ValidationError('Passwords did not match!')
        attrs['password'] = make_password(confirm_password)
        return attrs

    def validate_last_name(self, value):
        if not value.title():
            raise serializers.ValidationError("Last name is incorrect")
        return value

    def validate_first_name(self, value: str):
        if not value.title():
            raise serializers.ValidationError(" First name is incorrect")
        return value

    def validate_password(self, value):
        return make_password(value)


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'username', 'type'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'slug'
        read_only_fields = 'slug',

    def get_products_count(self, obj):
        return obj.products.count()


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = 'updated_at',
        read_only_fields = 'slug',

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category).data
        repr['owner'] = UserModelSerializer(instance.owner).data
        return repr
