from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'name', 'last_name', 'patronimic', 'phone']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['data', 'title']


class Pereval_addedSerializer(serializers.ModelSerializer):
    coords = CoordsSerializer()
    photo = PhotoSerializer()
    # устанавливает инфу о текущем юзере
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pereval_added
        # статус сам должен автоматически выставиться на new
        exclude = ['add_time', 'status']


# чтобы можно было проверить все
class PerevalSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    coords = CoordsSerializer()
    # photo = PhotoSerializer()
    user = UsersSerializer()

    class Meta:
        model = Pereval_added
        exclude = ['add_time']