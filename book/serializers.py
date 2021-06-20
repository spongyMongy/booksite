from rest_framework import serializers

from .models import Books
from .models import Opinions




class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        depth = 1


class OpinionsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Opinions
        fields = '__all__'
        depth = 1

