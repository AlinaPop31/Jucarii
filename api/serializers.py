from rest_framework import serializers
from . models import Jucarie, Categorie, Brand


class BrandSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')

class ListCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'nume')


class JucarieSerializer(serializers.ModelSerializer):
    categorii = ListCategorieSerializer(many=True, read_only=True)
    brand = BrandSerielizer()
    class Meta:
        model = Jucarie
        fields = ('id', 'categorii', 'varsta', 'brand')