from rest_framework import serializers
from mainapp.models import Movies

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class MovieSerializerNotId(serializers.ModelSerializer):
    class Meta:
        model = Movies
        # Exclude id from the request data and response
        # Avoinding user to change the pk=id however he wants
        exclude = ['id']

    def to_representation(self, instance):
        # Because the id is exclude is needed to return the id on the response
        data = super().to_representation(instance)
        data['id'] = instance.id

        # Reorder the field so id stays on top again
        ordered_data = {'id': data['id']}
        ordered_data.update(data)

        return ordered_data
