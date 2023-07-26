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
    # pereval = serializers.PrimaryKeyRelatedField(queryset=Pereval_added.objects.all())
    class Meta:
        model = Photo
        # fields = ['data', 'title', 'pereval']
        fields = '__all__'

# submitData
class Pereval_addedSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    coords = CoordsSerializer()
    # устанавливает инфу о текущем юзере
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = UsersSerializer()
    # photos = PhotoSerializer(required=False)
    photo = PhotoSerializer()

    class Meta:
        model = Pereval_added
        # статус сам должен автоматически выставиться на new
        exclude = ['add_time', 'status']


# чтобы можно было проверить все
class PerevalSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    coords = CoordsSerializer()
    # photo = PhotoSerializer()
    user = UsersSerializer()

    class Meta:
        model = Pereval_added
        exclude = ['add_time']